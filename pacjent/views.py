
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import ValidationError
from pacjent.forms import LoginForm, NewUserForm
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
            user = authenticate(pesel=pesel, password=password)
            if user:
                login(request, user)
            else:
                form.add_error(None, "Zły numer pesel lub hasło")
            return render(request, 'pacjentapp/login.html', {'form': form})
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
            if Patient.objects.filter(pesel=pesel).exists():
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
            new_patient = Patient.objects.create_user(pesel=pesel,
                                                      first_name=first_name,
                                                      last_name=last_name,
                                                      password=password,
                                                      date_of_birth=date_of_birth,
                                                      street=street,
                                                      build_number=build_number,
                                                      apartment_number=apartment_number,
                                                      post_code=post_code,
                                                      city=city,
                                                      mail=mail
                                                      )

            return redirect('mainview')
        return render(request, 'pacjentapp/add_patient.html', locals())
