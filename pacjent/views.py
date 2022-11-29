
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
            else:
                form.add_error(None, "Zły numer pesel lub hasło")
                return render(request, 'pacjentapp/login.html', {'form': form})
            return redirect('mainview')
#TODO: Change link after login


class MainView(View):
    def get(self, request):
        return render(request, 'pacjentapp/base_two.html')


class AddNewPatient(View):
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
            setting = new_patient.patient
            setting.pesel = pesel
            setting.date_of_birth = date_of_birth
            setting.street = street
            setting.build_number = build_number
            setting.apartment_number = apartment_number
            setting.post_code = post_code
            setting.city = city
            new_patient.save()

            return redirect('mainview')
        return render(request, 'pacjentapp/add_patient.html', locals())


class SearchPatientView(View):
    def get(self, request):
        form = SearchForm()
        return render(request, 'pacjentapp/searchpatient.html', locals())
    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data.get('pesel')
            user = User.objects.get(username=pesel)

