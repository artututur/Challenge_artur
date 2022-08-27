from pages.base_page import BasePage
import os

class LoginPage(BasePage):
    login_filed_xpath = "//*[@id='login']"
    password_filed_xpath = "//*[@id= 'password']"
    sign_in_button_xpath = "//*[text()= 'Sign in']"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = "Scouts panel - sign in"
    title_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    title_of_box = "Scouts Panel"
    invalid_date_xpath = "//*[@id='__next']/form/div/div[1]/div[3]/span"
    invalid_date = 'Identifier or password invalid.'
    sign_out_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    players_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    search_box_xpath = "//*[@id='__next']/div[1]/header/div/div[1]/div[2]/input"


    def type_in_email(self, email):
        self.field_send_keys(self.login_filed_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_filed_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def check_title_of_box(self):
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.title_of_box)

    def check_write_invalid_date(self):
        self.assert_element_text(self.driver, self.invalid_date_xpath, self.invalid_date)

    def click_on_the_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def type_in_search_box(self, search):
        self.field_send_keys(self.search_box_xpath, search)

    def click_on_the_players(self):
        self.click_on_the_element(self.players_button_xpath)


