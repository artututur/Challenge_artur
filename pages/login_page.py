from pages.base_page import BasePage


class LoginPage(BasePage):
    login_filed_xpath = "//*[@id='login']"
    password_filed_xpath = "//*[@id= 'password']"
    sign_in_button_xpath = "//*[text()= 'Sign in']"


    def type_in_email(self, email):
        self.field_send_keys(self.login_filed_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_filed_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)




