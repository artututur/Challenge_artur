import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl'
    element_text = 'Scouts Panel'
    element_text_xpath = "//*[@id='__next']/div[1]/header/div/h6"
    futbol_koletyw_logo_xpath = "//*[@title= 'Logo Scouts Panel']"
    button_change_language_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]"
    add_player_xpath = "//*[text() = 'Add player']"
    email_fill_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
    name_fill_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    surname_fill_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    phone_fill_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input"
    weight_fill_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
    height_fill_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
    age_fill_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input"
    leg_button_xpath = "//*[@id='mui-component-select-leg']"
    left_leg_button_xpath = "//*[text() = 'Left leg' and @role= 'option']"
    club_fill_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[9]/div/div/input"
    level_full_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input"
    main_position_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input"
    second_position_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[12]/div/div/input"
    district_button_xpath = "//*[@id='mui-component-select-district']"
    opole_button_xpath = "//*[@id='menu-district']/div[3]/ul/li[8]"
    achievements_xpath = "//*[ @ id = '__next']/div[1]/main/div[2]/form/div[2]/div/div[14]/div/div/input"
    submit_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]/span[1]"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.futbol_koletyw_logo_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def button_change_language(self):
        self.click_on_the_element(self.button_change_language_xpath)

    def button_add_player(self):
        self.click_on_the_element(self.add_player_xpath)

    def email_fill(self, email):
        self.field_send_keys(self.email_fill_xpath, email)

    def name_fill(self, name):
        self.field_send_keys(self.name_fill_xpath, name)

    def surname_fill(self, surname):
        self.field_send_keys(self.surname_fill_xpath, surname)

    def phone_fill(self, phone):
        self.field_send_keys(self.phone_fill_xpath, phone)

    def weight_fill(self, weight):
        self.field_send_keys(self.weight_fill_xpath, weight)

    def height_fill(self, height):
        self.field_send_keys(self.height_fill_xpath, height)

    def age_fill(self, age):
        self.field_send_keys(self.age_fill_xpath, age)

    def click_on_the_leg_button(self):
        self.click_on_the_element(self.leg_button_xpath)

    def click_on_the_left_leg_button(self):
        self.click_on_the_element(self.left_leg_button_xpath)

    def club_fill(self, club):
        self.field_send_keys(self.club_fill_xpath, club)

    def level_fill(self, level):
        self.field_send_keys(self.level_full_xpath, level)

    def main_position_fill(self, position):
        self.field_send_keys(self.main_position_xpath, position)

    def second_position_fill(self, position):
        self.field_send_keys(self.second_position_xpath, position)

    def district_button(self):
        self.click_on_the_element(self.district_button_xpath)

    def opole_button(self):
        self.click_on_the_element(self.opole_button_xpath)

    def achievements_fill(self,achievements):
        self.field_send_keys(self.achievements_xpath, achievements)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)
