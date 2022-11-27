from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required

from pacjent.forms import LoginForm
from pacjent.models import Patient


# Create your views here.


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'html/login.html', locals())
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
#TODO: render main web


@login_required
class MainView(View):
    pass