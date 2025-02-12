import pytest
from selenium import webdriver
import helper

@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    browser_name = request.param
    if browser_name == 'chrome':
        driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def user():
    user = helper.register_new_user_and_return_user_data()
    yield user
    helper.delete_user(user['json']['accessToken'])
