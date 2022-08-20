from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_xpath = "// span[contains(@class , 'MuiTypography') and text()= 'Main page']"
    players_xpath = "//*[@class= 'MuiListItemText-root jss29 jss31']"
    polski_xpath = "//*[text() = 'Polski']"
    sign_out_xpath = "//*[text() = 'Sign out']"
    players_count_xpath = "//*[text()= 'Players count']"
    matches_count_xpath = "//*[text()= 'Matches count']"
    reports_count_xpath = "//*[text()= 'Reports count']"
    events_count_xpath = "//*[text()= 'Events count']"
    scouts_pane_xpath = "//h2[text()= 'Scouts Panel']"
    shortcuts_xpath = "//span[text()= 'Add player']"
    activity_xpath = "//*[@href='/en/players/62f2bce6159aa3d4fa18f4b2/edit']"




