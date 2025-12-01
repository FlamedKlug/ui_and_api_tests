import allure
import pytest
from allure_commons.types import Severity
from pages.css_selectors import CssSelector
from pages.ixbt_page import IxbtPage

ixbt_css = CssSelector()
ixbt_page = IxbtPage()


@allure.tag("UI")
@allure.label("owner", "Klug")
@allure.feature("IXBT - Проверяем кук-информер - открыт")
@allure.story('Кук-информер должен быть виден')
@allure.severity(Severity.CRITICAL)
@pytest.mark.parametrize("browser_setup", ["ixbt"], indirect=True)
def test_cookies_agreement_is_visible(browser_setup):
    with allure.step("Открываем страницу в браузере"):
        ixbt_page.open()
    with allure.step("Соглашение по кукам отображено"):
        ixbt_page.should_visible(ixbt_css.cookies_popup)


@allure.tag("UI")
@allure.label("owner", "Klug")
@allure.feature("IXBT - Проверяем кук-информер - закрыт")
@allure.story('Кук-информер закрывается по крестику и более не виден')
@allure.severity(Severity.NORMAL)
@pytest.mark.parametrize("browser_setup", ["ixbt"], indirect=True)
def test_cookies_agreement_close(browser_setup):
    with allure.step("Открываем страницу в браузере"):
        ixbt_page.open()
    with allure.step("Закрываем соглашение по кукам"):
        ixbt_page.click_on_page(ixbt_css.cookies_popup_dismiss)
    with allure.step("Соглашение по кукам не отображается"):
        ixbt_page.should_not_visible(ixbt_css.cookies_popup)


@allure.tag("UI")
@allure.label("owner", "Klug")
@allure.feature("IXBT - Проверяем иконку ютуба")
@allure.story('Иконка ютуба не видна')
@allure.severity(Severity.TRIVIAL)
@pytest.mark.parametrize("browser_setup", ["ixbt"], indirect=True)
def test_youtube_icon_is_visible(browser_setup):
    with allure.step("Открываем страницу в браузере"):
        ixbt_page.open()
    with allure.step("Иконка Youtube видна"):
        ixbt_page.should_visible(ixbt_css.youtube_icon)


@allure.tag("UI")
@allure.label("owner", "Klug")
@allure.feature("IXBT - Проверяем иконку поиска")
@allure.story('Иконка поиска видна')
@allure.severity(Severity.CRITICAL)
@pytest.mark.parametrize("browser_setup", ["ixbt"], indirect=True)
def test_search_icon_is_visible(browser_setup):
    with allure.step("Открываем страницу в браузере"):
        ixbt_page.open()
    with allure.step("Иконка поиска видна"):
        ixbt_page.should_visible(ixbt_css.search_icon)


@allure.tag("UI")
@allure.label("owner", "Klug")
@allure.feature("IXBT - Проверяем поиск")
@allure.story('Инпут поиска виден')
@allure.severity(Severity.CRITICAL)
@pytest.mark.parametrize("browser_setup", ["ixbt"], indirect=True)
def test_search_input_is_visible(browser_setup):
    with allure.step("Открываем страницу в браузере"):
        ixbt_page.open()
    with allure.step("Клик на иконку поиска"):
        ixbt_page.click_on_page(ixbt_css.search_icon)
    with allure.step("Видна строка поиска"):
        ixbt_page.should_visible(ixbt_css.search_input)


@allure.tag("UI")
@allure.label("owner", "Klug")
@allure.feature("IXBT - Проверяем кнопку авторизации")
@allure.story('Кнопка авторизации отображается')
@allure.severity(Severity.BLOCKER)
@pytest.mark.parametrize("browser_setup", ["ixbt"], indirect=True)
def test_authorization_button_is_visible(browser_setup):
    with allure.step("Открываем страницу в браузере"):
        ixbt_page.open()
    with allure.step("Кнопка авторизации отображается"):
        ixbt_page.should_visible(ixbt_css.authorization_button)


@allure.tag("UI")
@allure.label("owner", "Klug")
@allure.feature("IXBT - Проверяем раздел новостей")
@allure.story('Новости открываются и имеют указанный заголовок')
@allure.severity(Severity.MINOR)
@pytest.mark.parametrize("browser_setup", ["ixbt"], indirect=True)
def test_news_page_have_subject(browser_setup):
    with allure.step("Открываем страницу в браузере"):
        ixbt_page.open()
    with allure.step("Клик на меню Новости"):
        ixbt_page.click_on_page(ixbt_css.news)
    with allure.step("Отображается заголовок Главные новости"):
        ixbt_page.should_have_text(ixbt_css.news_subject, "новости")
