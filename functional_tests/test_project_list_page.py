from selenium import webdriver
from selenium.webdriver.common.by import By
from pacjent.models import Doctor
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

class TestProjectListPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_login_is_displayed(self):
        self.browser.get(self.live_server_url)

        # The user login to system
        alert = self.browser.find_element(By.CLASS_NAME, 'logins')
        self.assertEquals(
            alert.find_element(By.TAG_NAME, 'h2').text,
            'Zaloguj się do konta'
        )