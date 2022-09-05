import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddingAPlayerToTheDatabase(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.check_title_of_box()
        user_login.type_in_email('user03@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.button_add_player()
        dashboard_page.email_fill('test-testowski@gmail.com')
        dashboard_page.name_fill('Test')
        dashboard_page.surname_fill('Testowski')
        dashboard_page.phone_fill('123456789')
        dashboard_page.weight_fill('66')
        dashboard_page.height_fill('180')
        dashboard_page.age_fill('25091998')
        dashboard_page.click_on_the_leg_button()
        dashboard_page.click_on_the_left_leg_button()
        dashboard_page.club_fill('WKS')
        dashboard_page.level_fill('666')
        dashboard_page.main_position_fill('Trener')
        dashboard_page.second_position_fill('Trener na wakacjach')
        dashboard_page.district_button()
        dashboard_page.opole_button()
        dashboard_page.achievements_fill("Mistrz swiata")
        dashboard_page.click_on_the_submit_button()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
