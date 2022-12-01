from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm


def post_code_validation(post_code):
    """
    :param post_code: system check if the post code is correct
    :return: if post code is wrong, system return information with error
    """
    if len(post_code) == 5:
        raise ValidationError("Kod pocztowy musi być w formacie 00-000")
    if post_code[2] != '-':
        raise ValidationError("Kod pocztowy musi być w formacie 00-000")


def pesel_validation(pesel):
    """
    :param pesel: Polish id
    :return: information about valid pesel
    """
    if len(pesel) != 11:
        raise ValidationError("PESEL ma 11 liczb!")
    elif len(pesel) == 11:
        tab = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
        suma = 0
        j = 0
        pesel = list(pesel)
        pesel_list = []
        while j < 11:
            pesel_list.append(int(pesel[j]))
            j += 1
        control_number = (pesel_list[-1])
        i = 0
        while i < len(tab):
            suma += int(pesel_list[i]) * tab[i]
            i += 1

        suma = suma % 10
        if (10 - suma) % 10 != control_number:
            raise ValidationError("PESEL jest niepoprawny!")


class NewUserForm(forms.Form):
    """
    :return Form : When admin or staff want add new user. This form is only use for staff
    """
    pesel = forms.CharField(max_length=11, required=True, validators=[pesel_validation])
    first_name = forms.CharField(max_length=64, required=True)
    last_name = forms.CharField(max_length=64, required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput, required=True)
    password_repeat = forms.CharField(max_length=32, widget=forms.PasswordInput, required=True)
    date_of_birth = forms.DateField(required=True)
    street = forms.CharField(max_length=128, required=True)
    build_number = forms.CharField(max_length=8, required=True)
    apartment_number = forms.CharField(max_length=8, empty_value=None, required=False)
    post_code = forms.CharField(max_length=6, validators=[post_code_validation], required=True)
    city = forms.CharField(max_length=128, required=True)
    mail = forms.EmailField(required=True)
#TODO: Zmiana hasła na autogenerowanie i pobieranie do pliku hasła.

class ChangeUserDataForm(forms.Form):
    """
    :return Form : When patient want change his data
    """
    street = forms.CharField(max_length=128, required=True)
    build_number = forms.CharField(max_length=8, required=True)
    apartment_number = forms.CharField(max_length=8, required=True)
    post_code = forms.CharField(max_length=6, validators=[post_code_validation], required=True)
    city = forms.CharField(max_length=128, required=True)


class LoginForm(forms.Form):
    """
    :return Form : login form
    """
    pesel = forms.CharField(max_length=11)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)


class SearchForm(forms.Form):
    """
    :return Form : if staff want search patient and all data about him
    """
    pesel = forms.CharField(max_length=11, required=True, validators=[pesel_validation])


class TestResultForm(forms.Form):
    patient = forms.CharField(max_length=11)
