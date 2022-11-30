import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import ValidationError
from pacjent.forms import LoginForm, NewUserForm, SearchForm
from pacjent.models import Patient


# Create your views here.


class LoginView(View):
    """
    GET: when user into website
    POST: when user text pesel and password, system checks which data is valid
    """
    def get(self, request):
        form = LoginForm()
        return render(request, 'pacjentapp/login.html', locals())

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data.get('pesel')
            password = form.cleaned_data.get('password')
            user = authenticate(username=pesel, password=password)
            if user:
                login(request, user)
                user.last_login = datetime.datetime.now()
            else:
                form.add_error(None, "Zły numer pesel lub hasło")
                return render(request, 'pacjentapp/login.html', {'form': form})
            return redirect('dashboard')
    ##TODO: Change link after login


class Dashboard(View):
    """
    GET: this is main view for users and staff
    """
    def get(self, request):
        return render(request, 'pacjentapp/base_two.html', locals())


class AddNewPatient(View):
    """
    Function : only staff have access to the content
    GET: when staff want add new patient
    POST: if staff click the button and all data is correct, we will add new patient to database.
        new_patient : create account user in User
        profile.user : assigning the User model to the Patient model
    """
    def get(self, request):
        form = NewUserForm()
        return render(request, 'pacjentapp/add_patient.html', locals())

    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data.get('pesel')
            if User.objects.filter(username=pesel).exists():
                raise ValidationError('Ten pacjent jest już w systemie!')
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            if password != password_repeat:
                raise ValidationError('Hasła nie są takie same!')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            street = form.cleaned_data.get('street')
            build_number = form.cleaned_data.get('build_number')
            apartment_number = form.cleaned_data.get('apartment_number')
            post_code = form.cleaned_data.get('post_code')
            city = form.cleaned_data.get('city')
            mail = form.cleaned_data.get('mail')

            new_patient = User.objects.create_user(username=pesel,
                                                   first_name=first_name,
                                                   last_name=last_name,
                                                   password=password,
                                                   email=mail)
            profile = Patient()
            profile.user = new_patient
            new_patient.patient.pesel = pesel
            new_patient.patient.date_of_birth = date_of_birth
            new_patient.patient.street = street
            new_patient.patient.build_number = build_number
            new_patient.patient.apartment_number = apartment_number
            new_patient.patient.post_code = post_code
            new_patient.patient.city = city
            profile.save()

            return redirect('dashboard')
        return render(request, 'pacjentapp/add_patient.html', locals())


class SearchPatientView(View):
    def get(self, request):
        form = SearchForm()
        return render(request, 'pacjentapp/searchpatient.html', locals())

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data.get('pesel')
            if User.objects.filter(username=pesel):
                user = User.objects.get(username=pesel)
                return render(request, 'pacjentapp/profilsearch.html', locals())
            else:
                return render(request, 'pacjentapp/searchpatient.html', {'form': SearchForm(),
                                                                         'error': 'Nie ma takiego pacjenta!'})
