from pages.login import LoginPage
import pytest

@pytest.mark.smoke
def test_valid_login(setup_and_teardown):
    lp = LoginPage(setup_and_teardown)
    lp.click_login_link()
    lp.enter_email_address("pradipta@gmail.com")
    lp.enter_password("123456")
    lp.click_login_btn()

@pytest.mark.regression
def test_invalid_login(setup_and_teardown):
    lp = LoginPage(setup_and_teardown)
    lp.click_login_link()
    lp.enter_email_address("pradiptagmail.com")
    lp.enter_password("1@")
    lp.click_login_btn()
