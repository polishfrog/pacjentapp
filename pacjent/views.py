import datetime
import random

import barcode
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin

import local_settings
from pacjent.forms import LoginForm, NewUserForm, SearchForm, TestResultForm, SortDataDashboardForm
from pacjent.models import Patient, TestResultPatient

#pdf
from reportlab.pdfgen import canvas
from django.http import HttpResponse


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


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class Dashboard(LoginRequiredMixin, View):
    """
    GET: this is main view for users and staff
    """
    login_url = '/'
    redirect_field_name = 'login'

    def get(self, request):
        #if TestResultPatient.objects.filter(patient=request.user.patient.pesel):
        search_type = 'date_test'
        test_check = [1, 2, 3, 4, 5, 6]

        formers = SortDataDashboardForm(request.GET)

        if formers.is_valid():
            search_type = formers.cleaned_data.get('search_option')
            test_check = formers.cleaned_data.get('test_check')

        if search_type == "date_test" or search_type == "name_test":
            search_all = "-" + search_type
            result = TestResultPatient.objects.filter(patient_id=request.user.id, name_test__in=test_check).order_by(search_all, "-date_test")
        else:
            search_all = "-" + search_type[0:9]
            result = TestResultPatient.objects.filter(patient_id=request.user.id, name_test__in=test_check).order_by(search_all, "date_test").reverse()

        formers = SortDataDashboardForm(initial={"search_option": search_type, "test_check": test_check})
        return render(request, 'pacjentapp/base_two.html', locals())


def generator_passwor():
    """Generated password for patient"""
    small_letter = "abcdefghijklmnoprstuwvxyz"
    big_latter = "ABCDEFGHIJKLMNOPRSTUWVXYZ"
    number = "0123456789"
    special_char = "!@#$"

    alls = small_letter + big_latter + number + special_char
    length = 16
    password = "".join(random.sample(alls, length))
    return password


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
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            street = form.cleaned_data.get('street')
            build_number = form.cleaned_data.get('build_number')
            apartment_number = form.cleaned_data.get('apartment_number')
            post_code = form.cleaned_data.get('post_code')
            city = form.cleaned_data.get('city')
            mail = form.cleaned_data.get('mail')
            password = generator_passwor()
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


            """Generate pdf file for patient"""
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline;'
            pdf = canvas.Canvas(response)
            pdf.drawString(150, 800, f'Login i haslo do zalogowania sie na platformie pacjent.pl')
            pdf.drawString(240, 780, f'Login: {pesel}')
            pdf.drawString(225, 760, f'Haslo: {password}')
            pdf.drawString(130, 740, f'Nie zgub swoich danych! Pamietaj, haslo jest przypisane na stale')
            pdf.showPage()
            pdf.save()
            return response
        return render(request, 'pacjentapp/add_patient.html', locals())

    def path(self):
        pass


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
                wyniki = TestResultPatient.objects.filter(patient=user.id)
                return render(request, 'pacjentapp/profilsearch.html', locals())
            else:
                return render(request, 'pacjentapp/searchpatient.html', {'form': SearchForm(),
                                                                         'error': 'Nie ma takiego pacjenta!'})


class AddTestResultView(View):
    def get(self, request):
        form = TestResultForm(initial={'test': 0})
        return render(request, 'pacjentapp/add_test.html', {'form': TestResultForm()})

    def post(self, request):
        form = TestResultForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data.get('pesel')
            if not User.objects.filter(username=pesel):
                return render(request, 'pacjentapp/add_test.html', {'form': TestResultForm(),
                                                                    'error': 'Taki użytkownik nie istnieje!'})

            name_test = form.cleaned_data.get('test')
            date_test = form.cleaned_data.get('data')
            leukocytes = form.cleaned_data.get('leukocytes')
            erythrocytes = form.cleaned_data.get('erythrocytes')
            hemoglobin = form.cleaned_data.get('hemoglobin')
            hematocrit = form.cleaned_data.get('hematocrit')
            mcv = form.cleaned_data.get('mcv')
            mch = form.cleaned_data.get('mch')
            mchc = form.cleaned_data.get('mchc')
            thrombocytes = form.cleaned_data.get('thrombocytes')
            rdw = form.cleaned_data.get('rdw')
            pdw = form.cleaned_data.get('pdw')
            plcr = form.cleaned_data.get('plcr')
            neutrophils = form.cleaned_data.get('neutrophils')
            volume = form.cleaned_data.get('volume')
            specific_gravity = form.cleaned_data.get('specific_gravity')
            color = form.cleaned_data.get('color')
            smell = form.cleaned_data.get('smell')
            look = form.cleaned_data.get('look')
            ph = form.cleaned_data.get('ph')
            glucose = form.cleaned_data.get('glucose')
            protein = form.cleaned_data.get('protein')
            nitrites = form.cleaned_data.get('nitrites')
            ketone_bodies = form.cleaned_data.get('ketone_bodies')
            bilirubin = form.cleaned_data.get('bilirubin')
            urobilinogen = form.cleaned_data.get('urobilinogen')
            glassy_rods = form.cleaned_data.get('glassy_rods')
            epithelial_rollers = form.cleaned_data.get('epithelial_rollers')
            erythrocytes_casts = form.cleaned_data.get('erythrocytes_casts')
            leukocyte_casts = form.cleaned_data.get('leukocyte_casts')
            grain_rolls = form.cleaned_data.get('grain_rolls')
            flat_epithelium = form.cleaned_data.get('flat_epithelium')
            round_epithelium = form.cleaned_data.get('round_epithelium')
            bacteria = form.cleaned_data.get('bacteria')
            yeast = form.cleaned_data.get('yeast')
            oxalates = form.cleaned_data.get('oxalates')
            soaked = form.cleaned_data.get('soaked')
            phosphates = form.cleaned_data.get('phosphates')

            wyniki = TestResultPatient()
            wyniki.patient = Patient.objects.get(pesel=pesel)
            wyniki.name_test = name_test
            wyniki.date_test = date_test
            wyniki.leukocytes = leukocytes
            wyniki.erythrocytes = erythrocytes
            wyniki.hemoglobin = hemoglobin
            wyniki.hematocrit = hematocrit
            wyniki.mcv = mcv
            wyniki.mch = mch
            wyniki.mchc = mchc
            wyniki.thrombocytes = thrombocytes
            wyniki.rdw = rdw
            wyniki.pdw = pdw
            wyniki.plcr = plcr
            wyniki.neutrophils = neutrophils
            wyniki.volume = volume
            wyniki.specific_gravity = specific_gravity
            wyniki.color = color
            wyniki.smell = smell
            wyniki.look = look
            wyniki.ph = ph
            wyniki.glucose = glucose
            wyniki.protein = protein
            wyniki.nitrites = nitrites
            wyniki.ketone_bodies = ketone_bodies
            wyniki.bilirubin = bilirubin
            wyniki.urobilinogen = urobilinogen
            wyniki.glassy_rods = glassy_rods
            wyniki.epithelial_rollers = epithelial_rollers
            wyniki.erythrocytes_casts = erythrocytes_casts
            wyniki.leukocyte_casts = leukocyte_casts
            wyniki.grain_rolls = grain_rolls
            wyniki.flat_epithelium = flat_epithelium
            wyniki.round_epithelium = round_epithelium
            wyniki.bacteria = bacteria
            wyniki.yeast = yeast
            wyniki.oxalates = oxalates
            wyniki.soaked = soaked
            wyniki.phosphates = phosphates

            wyniki.save()
            return render(request, 'pacjentapp/add_test.html', {'form': TestResultForm(),
                                                                'error': 'Wyniki poprawnie dodane!'})

        return render(request, 'pacjentapp/add_test.html', {'form': TestResultForm(),
                                                            'error': 'Błąd!'})


class ResultTest(View):
    def get(self, request, number_test):
        wynik = TestResultPatient.objects.get(id=number_test)

        if wynik.patient_id != request.user.id:
            return redirect('dashboard')
        return render(request, 'pacjentapp/test_result_info.html', {'wynik': wynik})

