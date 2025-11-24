import pytest
import requests
from allure_commons._allure import step
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.authorization import AuthorizationData
from utils import attach
import os
from dotenv import load_dotenv

BASE_URL_IXBT = "https://www.ixbt.com"
BASE_URL_DEMOSHOP = "https://demowebshop.tricentis.com"
BASE_AUTH_COOKIE_NAME = "NOPCOMMERCE.AUTH"


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', params=["ixbt", "demoshop"])
def browser_setup(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f'https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub',
        options=options)
    browser.config.driver = driver
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    if request.param == "ixbt":
        browser.config.base_url = BASE_URL_IXBT
    if request.param == "demoshop":
        browser.config.base_url = BASE_URL_DEMOSHOP

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope='function')
def auth_cookies():
    auth_data = AuthorizationData()
    auth_data.login = os.getenv("DEMOWEBSHOP_LOGIN")
    auth_data.password = os.getenv("DEMOWEBSHOP_PASS")
    auth_data.remember = False
    with step("Авторизация по API"):
        result = requests.post(
            url=BASE_URL_DEMOSHOP + "/login",
            data={"Email": auth_data.login, "Password": auth_data.password, "RememberMe": auth_data.remember},
            allow_redirects=False
        )
    with step("Сохранили куки из API"):
        auth_data.cookie = result.cookies.get(BASE_AUTH_COOKIE_NAME)

    yield auth_data

    attach.add_api_response_attaching(result.request, result, auth_data)
