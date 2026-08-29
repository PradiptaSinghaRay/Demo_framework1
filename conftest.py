from selenium import webdriver
import pytest


# @pytest.fixture
#
# def setup_and_teardown():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("http://demowebshop.tricentis.com/")
#     yield driver
#     driver.quit()


@pytest.fixture

def setup_and_teardown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.bmrc.co.in/")
    yield driver
    driver.quit()