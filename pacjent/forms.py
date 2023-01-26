from django import forms
from django.core.exceptions import ValidationError
import re
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


TEST = (
    (0, "---------"),
    (1, "Badanie krwi"),
    (2, "Badanie moczu"),
    (3, "Morfologia"),
    (4, "Glukoza"),
    (5, "Próby wątrobowe"),
    (6, "Badanie kreatyny"),
)

TEST_FORM = (
    (1, "Badanie krwi"),
    (2, "Badanie moczu"),
    (3, "Morfologia"),
    (4, "Glukoza"),
    (5, "Próby wątrobowe"),
    (6, "Badanie kreatyny"),
)


class TestResultForm(forms.Form):
    pesel = forms.CharField(max_length=11, required=True, label="PESEL")
    test = forms.ChoiceField(choices=TEST, required=True, label="Rodzaj testu", )
    data = forms.DateField(required=True, label="Data wykonania testu", help_text="Standardowe wartości:")
    leukocytes = forms.FloatField(required=False, label="Leukocyty", help_text="Krew: 4.1 - 10.9 | Mocz: 1 - 4 ")
    erythrocytes = forms.FloatField(required=False, label="Erytrocyty", help_text="Krew: 3.9-6.5 | Mocz: 0 - 1")
    hemoglobin = forms.FloatField(required=False, label="Hemoglobina", help_text="Krew: 11.5-17.5", min_value=5)
    hematocrit = forms.IntegerField(required=False, label="Hematokryt", help_text="Krew: 37-52%")
    mcv = forms.IntegerField(required=False, help_text="Krew: 80-97 fl")
    mch = forms.IntegerField(required=False, help_text="Krew: 26-33 pg")
    mchc = forms.IntegerField(required=False, help_text="Krew: 32-36 g/dl")
    thrombocytes = forms.IntegerField(required=False, label="Trombocyty (płytki krwi, PLT)",
                                      help_text="Krew: 150-450 tys/ul")
    rdw = forms.FloatField(required=False, help_text="Krew: 11.5-14.5%")
    pdw = forms.IntegerField(required=False, help_text="Krew: 8-13 fl")
    plcr = forms.IntegerField(required=False, help_text="Krew: 13-43%")
    neutrophils = forms.IntegerField(required=False, label="Neutrofile (NEUT)", help_text="Krew: 50-70%")

    volume = forms.IntegerField(required=False, label="Objętość", help_text="Mocz: 400-1800 ml")
    specific_gravity = forms.IntegerField(required=False, label="Ciężar właściwy", help_text="Mocz: 1015-1030 g/ml")
    color = forms.CharField(required=False, max_length=64, label="Kolor", help_text="Mocz: słomkowożółty")
    smell = forms.CharField(required=False, max_length=64, label="Zapach", help_text="Mocz: nieznaczny")
    look = forms.CharField(required=False, max_length=64, label="Wygląd", help_text="Mocz: przejrzysty")
    ph = forms.FloatField(required=False, help_text="Mocz: 4,8 - 7,4")
    glucose = forms.FloatField(required=False, label="Glukoza", help_text="Mocz: <15 mg/dl")
    protein = forms.FloatField(required=False, label="Białko", help_text="Mocz: <10 mg/dl")
    nitrites = forms.CharField(required=False, max_length=64, label="Azotyny", help_text="Mocz: nieobecne")
    ketone_bodies = forms.FloatField(required=False, label="Ciała ketonowe", help_text="Mocz: <5 mg/dl")
    bilirubin = forms.FloatField(required=False, label="Bilirubina", help_text="Mocz: <0,2 mg/dl")
    urobilinogen = forms.FloatField(required=False, label="Urobilinogen", help_text="Mocz: <1 mg/dl")
    glassy_rods = forms.FloatField(required=False, label="Wałeczki szkliste", help_text="Mocz: 0 - 1")
    epithelial_rollers = forms.CharField(required=False, max_length=64, label="Wałeczki nabłonkowe",
                                         help_text="Mocz: nieobecne")
    erythrocytes_casts = forms.CharField(required=False, max_length=64, label="Wałeczki erytrocytarne",
                                         help_text="Mocz: nieobecne")
    leukocyte_casts = forms.CharField(required=False, max_length=64, label="Wałeczki leukocytarne",
                                      help_text="Mocz: nieobecne")
    grain_rolls = forms.CharField(required=False, max_length=64, label="Wałeczki ziarniste",
                                  help_text="Mocz: nieobecne")
    flat_epithelium = forms.FloatField(required=False, label="Nabłonki płaskie", help_text="Mocz: 5-15")
    round_epithelium = forms.CharField(required=False, max_length=64, label="Nabłonki okrągłe",
                                       help_text="Mocz: nieobecne")
    bacteria = forms.CharField(required=False, max_length=64, label="Bakteria", help_text="Mocz: nieobecne")
    yeast = forms.CharField(required=False, max_length=64, label="Drożdżaki", help_text="Mocz: nieobecne")
    oxalates = forms.CharField(required=False, max_length=64, label="Szczawiany", help_text="Mocz: obecne")
    soaked = forms.CharField(required=False, max_length=64, label="Moczany", help_text="Mocz: obecne")
    phosphates = forms.CharField(required=False, max_length=64, label="Fosforany", help_text="Mocz: obecne")


SEARCH_OPTION = (
    ("date_test", "Data rosnąco"),
    ("date_test_reverse", "Data malejąco"),
    ("name_test", "Nazwa badania rosnąco"),
    ("name_test_reverse", "Nazwa badania malejąco"),
)


class SortDataDashboardForm(forms.Form):
    test_check = forms.MultipleChoiceField(choices=TEST_FORM, label="Rodzaj badania", widget=forms.CheckboxSelectMultiple)
    search_option = forms.ChoiceField(choices=SEARCH_OPTION, label="Filtruj")


