import allure
import pytest
import requests
from allure_commons._allure import step
from allure_commons.types import Severity
from selene import browser
from selene.support.conditions import have
from conftest import BASE_URL_DEMOSHOP, BASE_AUTH_COOKIE_NAME
from utils import attach


@allure.tag("API")
@allure.label("owner", "Klug")
@allure.feature("DEMOSHOP - Проверяем авторизацию")
@allure.story('После авторизации видим введенную почту')
@allure.severity(Severity.BLOCKER)
@pytest.mark.parametrize("browser_setup", ["demoshop"], indirect=True)
def test_authorization(auth_cookies, browser_setup):
    with step("Успешная авторизация"):
        browser.open(BASE_URL_DEMOSHOP)
        browser.driver.add_cookie({"name": BASE_AUTH_COOKIE_NAME, "value": auth_cookies.cookie})
        browser.open(BASE_URL_DEMOSHOP)
        browser.element(".account").should(have.text(auth_cookies.login))


@allure.tag("API")
@allure.label("owner", "Klug")
@allure.feature("DEMOSHOP - Добавление товара в корзину")
@allure.story('Счетчик товаров после добавления = 1')
@allure.severity(Severity.CRITICAL)
@pytest.mark.parametrize("browser_setup", ["demoshop"], indirect=True)
def test_basket_add_one_position(auth_cookies, browser_setup):
    with step("Добавление товара в корзину через API"):
        session = requests.Session()
        response = session.post(
            BASE_URL_DEMOSHOP + "/addproducttocart/catalog/31/1/1"
        )
        assert response.status_code == 200
        attach.response_allure_attaching(response)
        attach.response_console_loggin(response)
    with step("Счетчик корзины = 1 после добавления товара"):
        browser.open(BASE_URL_DEMOSHOP + '/cart')
        # Прокидываем куки
        for cookie in session.cookies:
            browser.driver.add_cookie({
                'name': cookie.name,
                'value': cookie.value,
                'path': '/'
            })

        browser.driver.refresh()
        browser.open(BASE_URL_DEMOSHOP + "/cart")
        browser.element(".cart-qty").should(have.text("(1)"))


@allure.tag("API")
@allure.label("owner", "Klug")
@allure.feature("DEMOSHOP - Очистка корзины")
@allure.story('После очистки корзины счетчик товаров = 0')
@allure.severity(Severity.NORMAL)
@pytest.mark.parametrize("browser_setup", ["demoshop"], indirect=True)
def test_basket_erase(auth_cookies, browser_setup):
    with step("Очистка корзины"):
        session = requests.Session()
        response = session.post(
            BASE_URL_DEMOSHOP + "/cart",
            data={
                'itemquantity5978448': '0',
                'updatecart': 'Update shopping cart',
                'discountcouponcode': '',
                'giftcardcouponcode': '',
                'CountryId': '0',
                'StateProvinceId': '0',
                'ZipPostalCode': ''
            }
        )
        assert response.status_code == 200
        attach.response_allure_attaching(response)
    with step("Счетчик корзины = 0 после очистки корзины"):
        browser.open(BASE_URL_DEMOSHOP + "/cart")
        browser.driver.add_cookie({"name": BASE_AUTH_COOKIE_NAME, "value": auth_cookies.cookie})
        browser.open(BASE_URL_DEMOSHOP + "/cart")
        browser.element(".cart-qty").should(have.text("(0)"))
