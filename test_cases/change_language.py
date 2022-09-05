import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestChangeLanguage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_change_language(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.check_title_of_box()
        user_login.type_in_email('user03@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.button_change_language()
        time.sleep(5)

#    def test_button_change_language(self):
#      time.sleep(10)
#      dashboard_page = Dashboard(self.driver)
#      dashboard_page.button_change_language()


    @classmethod
    def tearDown(self):
        self.driver.quit()
