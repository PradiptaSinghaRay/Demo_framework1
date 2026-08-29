from Framework_1.pages.register import RegisterPage
import pytest

@pytest.mark.smoke
def valid_register(setup_and_teardown):
    Rp = RegisterPage(setup_and_teardown)
    Rp.click_register_link()
    Rp.click_gender()
    Rp.click_first_name("pradipta")
    Rp.click_last_name("singha ray")
    Rp.click_email("pradiptasingharay01@gmail.com")
    Rp.click_password("123456")
    Rp.click_confirm_password("123456")
    Rp.click_register_button()