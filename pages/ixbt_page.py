from selene import have, by
from selene.support.shared import browser
from selene.support.conditions import be
from selene.support.shared.jquery_style import s


class IxbtPage:

    @staticmethod
    def open():
        browser.open("/")

    @staticmethod
    def should_visible(css_selector):
        s(by.css(css_selector)).should(be.visible)

    @staticmethod
    def should_not_visible(css_selector):
        s(by.css(css_selector)).should(be.not_.visible)

    @staticmethod
    def should_have_text(css_selector, have_text):
        s(css_selector).should(have.text(have_text))

    @staticmethod
    def click_on_page(css_selector):
        s(css_selector).click()
