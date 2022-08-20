from pages.base_page import BasePage


class LoginPage(BasePage):
    scouts_Panel_xpath = "//*[text()="Scouts Panel"]"
    login_xpath = "//*[@id="login-label"]"
    password_xpath = "//label[text()= "Password"]"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
