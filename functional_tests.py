import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisionTest(unittest.TestCase):

    def setUp(self):
        """Start test (open web)"""
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """End test (close web)"""
        self.browser.quit()

    def test_open_login_site(self):
        """When user enter to website"""
        self.browser.get('http://127.0.0.1:8000/')

        self.assertIn('Login', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h2')
        self.assertIn('Zaloguj', header_text.text)

        login_form = self.browser.find_element(By.ID, 'id_pesel')
        login_form.send_keys('01212302357')
        password_form = self.browser.find_element(By.ID, 'id_password')
        password_form.send_keys('e15jw%5t5flp#!6')
        password_form.send_keys(Keys.ENTER)

        time.sleep(2)

        self.assertIn('Portal', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')