from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath =
    sign_in_button_xpath =

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
Scouts_Panel_xpath= "//*[text()="Scouts Panel"]"
Scouts_Panel_xpath= "//h5[contains(@class, "MuiTypography")]"
Scouts_Panel_xpath= "//*[@id="__next"]/form/div/div[1]/h"


Login_xpath= "//*[@id="login-label"]"
Login_xpath= "//label[text()="Login"]"
Login_xpath= "//*[@for= "login" and @id= "login-label"]"


Password_xpath= "//label[text()= "Password"]"
Password_xpath= "//*[@for= "password" and @id= "password-label"]"
Password_xpath= "//label[contains(@class, "MuiFormLabel") and @for= "password"]"


Remind_password_xpath= "//*[text()= "Remind password"]"
Remind_password_xpath= "//a[contains(@class, "MuiTypography")]"
Remind_password_xpath" =//*[@id="__next"]/form/div/div[1]/a"


English_xpath= "//*[text()= "English"]"
English_xpath= "//*[@role= "button" and text()= "English"]"
English_xpath= "//*[@role= "button"]"


Polski_xpath= "//*[@role= "button" and text()= "Polski"]"
Polski_xpath= "//*[contains(@class, "MuiSelect") and text()= "Polski"]"
Polski_xpath= "//*[text()= "Polski"]"


Zaloguj_xpath= "//button[@type= "submit"]"
Zaloguj_xpath= "//*[contains(@class, "MuiButtonBase")]"
Zaloguj_xpath = "//button[@tabindex= "0"]"