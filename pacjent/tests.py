from django.test import SimpleTestCase, TestCase, Client
import pytest
from django.contrib.auth import get_user
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from pacjent.models import Patient, TestResultPatient, Place, Special, Doctor, DoctorInPlace, ReservationPatient, pesel_validation
import json
from pacjent.views import SearchPatientView, Dashboard, AddNewPatient, LoginView, AddTestResultView, Logout, ResultTest

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

    def test_login_two(self):
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

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.dashborad_url = reverse('dashboard')
        self.add_new_patient_url = reverse('add-new-patient')
        self.search_patient_url = reverse('search-patient')
        self.add_test_result_url = reverse('add-test-result')
        self.logout_url = reverse('logout')
        self.result_test_url = reverse('result-test', args=[1])

        #TestResultPatient.objects.create(
        #    patient = '01212302357',
        #    name_test = 1,
        #    date_test = '2022-12-15',
        #)

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

"""class TestSearchPatient(TestCase):

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
"""