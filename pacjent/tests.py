from django.test import TestCase, Client
import pytest
from django.contrib.auth import get_user
from django.urls import reverse
from django.contrib.auth.models import User
from pacjent.models import Patient, pesel_validation

# Create your tests here.




class TestView(TestCase):
    def test_search_patient(self):
        response = self.client.get(reverse('search-patient'))
        assert response.status_code == 200
        print("\nView Search-Patient is working")

    def test_dashboard(self):
        response = self.client.get(reverse('dashboard'))
        assert response.status_code == 302
        print("\nView Dashboard is working for only logged users")

    def test_add_new_patient(self):
        response = self.client.get(reverse('add-new-patient'))
        assert response.status_code == 200
        print("\nView Add-New-Patient is working")

    def test_login(self):
        response = self.client.get(reverse('login'))
        assert response.status_code == 200
        print("\nView Login is working")

    def test_add_test_result(self):
        response = self.client.get(reverse('add-test-result'))
        assert response.status_code == 200
        print(f"\nView Add-Test-Result is working")

    def test_logout(self):
        response = self.client.get(reverse('logout'))
        assert response.status_code == 302
        print("\nView Logout is working for only logged users")


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
