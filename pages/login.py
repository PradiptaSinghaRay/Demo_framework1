from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    login_link = (By.LINK_TEXT, 'Log in')
    email = (By.ID, 'Email')
    password = (By.ID, 'Password')
    login_btn = (By.XPATH, '(//input[@type="submit"])[2]')

    def click_login_link(self):
        self.click(self.login_link)

    def enter_email_address(self,email):
        self.enter_text(self.email,email)

    def enter_password(self,password):
        self.enter_text(self.password,password)

    def click_login_btn(self):
        self.click(self.login_btn)
