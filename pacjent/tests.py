from django.test import SimpleTestCase, TestCase, Client
import pytest
from django.contrib.auth import get_user
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from pacjent.models import Patient, TestResultPatient, Place, Special, Doctor, DoctorInPlace, ReservationPatient, pesel_validation
import json
from pacjent.views import SearchPatientView, Dashboard, AddNewPatient, LoginView, AddTestResultView, Logout, ResultTest
from pacjent.forms import NewUserForm, ChangeUserDataForm, LoginForm, SearchForm, TestResultForm
# Create your tests here.




class TestUrl(SimpleTestCase):
    """
        return : information about urls
    """
    def test_search_patient(self):
        url = reverse('search-patient')
        self.assertEquals(resolve(url).func.view_class, SearchPatientView)

    def test_dashboard(self):
        url = reverse('dashboard')
        self.assertEquals(resolve(url).func.view_class, Dashboard)

    def test_add_new_patient(self):
        url = reverse('add-new-patient')
        self.assertEquals(resolve(url).func.view_class, AddNewPatient)

    def test_login(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_add_test_result(self):
        url = reverse('add-test-result')
        self.assertEquals(resolve(url).func.view_class, AddTestResultView)

    def test_logout(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, Logout)

    #def test_result_test(self):
    #    url = reverse('result-test', args=['8'])
    #    self.asserEquals(resolve(url).func.view_class, ResultTest)


class TestViews(TestCase):
    """
        Test views with GET and POST method
    """

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.dashborad_url = reverse('dashboard')
        self.add_new_patient_url = reverse('add-new-patient')
        self.search_patient_url = reverse('search-patient')
        self.add_test_result_url = reverse('add-test-result')
        self.logout_url = reverse('logout')
        self.result_test_url = reverse('result-test', args=[1])



    def test_project_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)

    def test_project_dashboard_GET(self):
        response = self.client.get(self.dashborad_url)
        self.assertEquals(response.status_code, 302)

    def test_project_add_new_patient_GET(self):
        response = self.client.get(self.add_new_patient_url)
        self.assertEquals(response.status_code, 200)

    def test_project_search_patient_url_GET(self):
        response = self.client.get(self.search_patient_url)
        self.assertEquals(response.status_code, 200)

    def test_project_add_test_result_url_GET(self):
        response = self.client.get(self.add_test_result_url)
        self.assertEquals(response.status_code, 200)

    def test_project_logout_url_GET(self):
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code, 302)

    #def test_project_result_test_url_GET(self):
    #    response = self.client.get(self.result_test_url)
    #    self.assertEquals(response.status_code, 200)


    def test_project_add_test_result_url_POST(self):
        response = self.client.post(self.add_test_result_url, {
            'patient': '01212302357',
            'name_test': 1,
            'date_test': '2022-12-15',
        })

        self.assertEquals(response.status_code, 200)

    def test_project_search_patient_url_POST(self):
        response = self.client.post(self.search_patient_url, {
            'pesel': '01212302357'
        })
        self.assertEquals(response.status_code, 200)

    def test_project_add_new_patient_url_POST_one(self):
        response = self.client.post(self.add_new_patient_url, {
            'first_name': 'Dawid',
            'last_name': 'Różewski',
            'date_of_birth': '2002-01-23',
            'street': 'Paprotki',
            'build_number': '2b',
            'apartment_number': '',
            'post_code': '44-190',
            'city': 'Knurów',
            'mail': 'kapiszony_online@gamil.com',
        })
        self.assertEquals(response.status_code, 200)


class TestModels(TestCase):
    def setUp(self):
        self.place = Place.objects.create(
            id=1,
            name='kominiarza',
            street='Strzelców Opolskich',
            build_number='15b',
            apartment_number='234',
            post_code='44-194',
            city='Knurów'
        )

        self.special = Special.objects.create(
            name='Chirurg'
        )

        self.doctor = Doctor.objects.create(
            id=1,
            first_name='Mariusz',
            last_name='Pudzianowski',
            special=self.special
        )

        self.doctor_in_place = DoctorInPlace.objects.create(
            doctor=self.doctor,
            place=self.place,
            date_of_employment='2021-07-01',
        )

        self.new_patient = User.objects.create(
            username='0121230257',
            first_name='Dawid',
            last_name='Różewski',
            password='12345',
            email='pomidory.dot@interia.eu'
        )

        self.patient = Patient.objects.create(
            user=self.new_patient,
            pesel=self.new_patient.username,
            date_of_birth='2001-01-23',
            street='Pudziana',
            build_number='28F',
            apartment_number='7',
            post_code='44-230',
            city='Czerwionka',
        )

        self.test_result_patient = TestResultPatient.objects.create(
            patient=self.patient,
            name_test='Badanie krwi',
            date_test='2022-12-15',
        )


    def test_project_is_assigned_place_on_creation(self):
        self.assertEquals(self.place.name, 'kominiarza')
        self.assertEquals(self.place.id, 1)
        self.assertEquals(self.place.street, 'Strzelców Opolskich')
        self.assertEquals(self.place.build_number, '15b')
        self.assertEquals(self.place.apartment_number, '234')
        self.assertEquals(self.place.post_code, '44-194')
        self.assertEquals(self.place.city, 'Knurów')

    def test_project_is_assigned_special_on_creation(self):
        self.assertEquals(self.special.name, 'Chirurg')

    def test_project_is_assigned_doctor_on_creation(self):
        self.assertEquals(self.doctor.special, self.special)
        self.assertEquals(self.doctor.first_name, 'Mariusz')

    def test_project_is_assigned_doctor_in_place_on_creation(self):
        self.assertEquals(self.doctor_in_place.doctor, self.doctor)
        self.assertEquals(self.doctor_in_place.place, self.place)

    def test_project_is_assigned_patient_on_creation(self):
        self.assertEquals(self.patient.pesel, self.new_patient.username)
        self.assertEquals(self.new_patient.first_name, 'Dawid')
        self.assertEquals(self.patient.date_of_birth, '2001-01-23')

    def test_project_is_assigned_test_result_patient_on_creation(self):
        self.assertEquals(self.test_result_patient.name_test, 'Badanie krwi')


class TestForms(SimpleTestCase):

    def test_LoginFormfrom_valid_data(self):
        form = LoginForm(data={
            'pesel': '01212302357',
            'password': '12345'
        })
        self.assertTrue(form.is_valid())

    def test_LoginForm_from_no_data(self):
        form = LoginForm(data={})
        self.assertFalse(form.is_valid())

    def test_SearchForm_form_valid_data(self):
        form = SearchForm(data={
            'pesel': '01212302357'
        })
        self.assertTrue(form.is_valid())

    def test_SearchForm_form_no_data(self):
        form = SearchForm(data={})
        self.assertFalse(form.is_valid())

    def test_SearchForm_form_bad_data(self):
        form = SearchForm(data={
            'pesel': '02332'
        })
        self.assertFalse(form.is_valid())

    def test_TestResultForm_form_valid_data(self):
        form = TestResultForm(data={
            'pesel': '01212302357',
            'test': 1,
            'data': '2022-12-15'
        })
        self.assertTrue(form.is_valid())

    def test_TestResultForm_form_no_data(self):
        form = TestResultForm(data={})
        self.assertFalse(form.is_valid())

    def test_ChangeUserDataForm_form_valid_data(self):
        form = ChangeUserDataForm(data={
            'street': 'Kapelanska',
            'build_number': '254b',
            'apartment_number': '2',
            'post_code': '44-194',
            'city': 'Knurów'
        })
        self.assertTrue(form.is_valid())

    def test_ChangeUserDataForm_form_no_data(self):
        form = ChangeUserDataForm(data={})
        self.assertFalse(form.is_valid())

    def test_NewUserForm_form_valid_data(self):
        form = ChangeUserDataForm(data={
            'pesel': '01212302357',
            'first_name': 'Mariusz',
            'last_name': 'Frankowski',
            'date_of_birth': '2022-12-15',
            'street': 'Kościuszki',
            'build_number': '231',
            'apartment_number': '2',
            'post_code': '44-194',
            'city': 'Gliwice',
            'mail': 'dajprzyklad_@wp.pl'
        })
        self.assertTrue(form.is_valid())

    def test_NewUserForm_form_no_data(self):
        form = ChangeUserDataForm(data={})
        self.assertFalse(form.is_valid())

class TestSearchPatient(TestCase):

    def test_search_one(self):
        url = reverse('search-patient')
        response = self.client.post(url, {'pesel': '01212302357'})
        print("\nView Search-patient is working for 01212302357")
        assert response.status_code == 200

    def test_search_two(self):
        url = reverse('search-patient')
        response = self.client.post(url, {'pesel': '52032243795'})
        print("\nView Search-patient is working for 52032243795")
        assert response.status_code == 200


class TestAddResultTest(TestCase):

    def test_add_one(self):
        url = reverse('add-test-result')
        response = self.client.post(url, {'pesel': '01212302357', 'test': 1, 'data': '2022-12-13'})
        print("\nAdd test result is working")
        assert response.status_code == 200

    def test_add_two(self):
        url = reverse('add-test-result')
        response = self.client.post(url, {'pesel': '01212302357',
                                          'test': 1,
                                          'data': '2022-12-13',
                                          'leukocytes': 10.5,
                                          'erythrocytes': 5.5,
                                          'hemoglobin': 12.6})
        print("\nAdd test result is working")
        assert response.status_code == 200

    def test_add_three(self):
        url = reverse('add-test-result')
        response = self.client.post(url, {'pesel': '01212302357',
                                          'test': 2,
                                          'data': '2022-12-13'})
        print("\nAdd test result is working")
        assert response.status_code == 200

TEST_FIRST = (
    ('01212302357', 0),
    ('01212302358', 1),
    ('23421', 1),
    ('52032243795', 0),
)

@pytest.mark.parametrize("pesel, result", TEST_FIRST)
def test_pesel(pesel, result):
    assert pesel_validation(pesel) == result
    print("Wynik musi być(0-dobrze, 1-źle)")
    print(f"{pesel} - {result}")
