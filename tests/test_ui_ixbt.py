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
    with allure.step("Browser open"):
        ixbt_page.open()
    with allure.step("Cookies agreement is visible"):
        ixbt_page.should_visible(ixbt_css.cookies_popup)


@allure.tag("UI")
@allure.label("owner", "Klug")
@allure.feature("IXBT - Проверяем кук-информер - закрыт")
@allure.story('Кук-информер закрывается по крестику и более не виден')
@allure.severity(Severity.NORMAL)
@pytest.mark.parametrize("browser_setup", ["ixbt"], indirect=True)
def test_cookies_agreement_close(browser_setup):
    with allure.step("Browser open"):
        ixbt_page.open()
    with allure.step("Cookies agreement close"):
        ixbt_page.click_on_page(ixbt_css.cookies_popup_dismiss)
    with allure.step("Cookies agreement is not visible"):
        ixbt_page.should_not_visible(ixbt_css.cookies_popup)


@allure.tag("UI")
@allure.label("owner", "Klug")
@allure.feature("IXBT - Проверяем иконку ютуба")
@allure.story('Иконка ютуба не видна')
@allure.severity(Severity.TRIVIAL)
@pytest.mark.parametrize("browser_setup", ["ixbt"], indirect=True)
def test_youtube_icon_is_not_visible(browser_setup):
    with allure.step("Browser open"):
        ixbt_page.open()
    with allure.step("Youtube icon is not visible"):
        ixbt_page.should_not_visible(ixbt_css.youtube_icon)


@allure.tag("UI")
@allure.label("owner", "Klug")
@allure.feature("IXBT - Проверяем иконку поиска")
@allure.story('Иконка поиска не видна')
@allure.severity(Severity.BLOCKER)
@pytest.mark.parametrize("browser_setup", ["ixbt"], indirect=True)
def test_search_icon_is_not_visible(browser_setup):
    with allure.step("Browser open"):
        ixbt_page.open()
    with allure.step("Search icon is not visible"):
        ixbt_page.should_not_visible(ixbt_css.search_icon)


@allure.tag("UI")
@allure.label("owner", "Klug")
@allure.feature("IXBT - Проверяем раздел новостей")
@allure.story('Новости открываются и имеют указанный заголовок')
@allure.severity(Severity.MINOR)
@pytest.mark.parametrize("browser_setup", ["ixbt"], indirect=True)
def test_news_page_have_subject(browser_setup):
    with allure.step("Browser open"):
        ixbt_page.open()
    with allure.step("Open menu-item News"):
        ixbt_page.click_on_page(ixbt_css.news)
    with allure.step("Page should have subject"):
        ixbt_page.should_have_text(ixbt_css.news_subject, "Главные новости")
