from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):

    register_link = (By.LINK_TEXT, "Register")
    gender = (By.ID, "gender-male")
    first_name = (By.ID, "FirstName")
    last_name = (By.ID, "LastName")
    email = (By.ID, "Email")
    password = (By.ID, "Password")
    confirm_password = (By.ID, "ConfirmPassword")
    register_button = (By.ID, "register-button")

    def click_register_link(self):
        self.click(self.register_link)

    def click_gender(self):
        self.click(self.gender).click()

    def click_first_name(self, first_name):
        self.enter_text(self.first_name, first_name)

    def click_last_name(self, last_name):
        self.enter_text(self.last_name, last_name)

    def click_email(self, email):
        self.enter_text(self.email, email)

    def click_password(self, password):
        self.enter_text(self.password, password)

    def click_confirm_password(self, confirm_password):
        self.enter_text(self.confirm_password, self.password)

    def click_register_button(self):
        self.click(self.register_button).click()
