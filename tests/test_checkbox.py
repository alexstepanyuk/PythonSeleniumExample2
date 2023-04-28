# coding=utf-8
import pytest
from pages.checkbox_page import CheckBoxPage
from tests.base_test import BaseTest
from data.locators import CheckBoxPageLocators


class TestCheckBox(BaseTest):

    @pytest.fixture
    def load_pages(self):
        self.page = CheckBoxPage(self.driver, self.wait)
        self.page.go_to_checkbox_page()

    def test_title(self, load_pages):
        self.page.check_title("DEMOQA")

    def test_open(self, load_pages):
        self.page.choose(self.page.locator.HOME)
        self.page.choose(self.page.locator.DESKTOP)
        self.page.choose(self.page.locator.DOCUMENTS)
        self.page.choose(self.page.locator.DOWNLOADS)
        self.page.choose(self.page.locator.WORKSPACE)
        self.page.choose(self.page.locator.OFFICE)

    def test_click(self, load_pages):
        self.test_open(load_pages)
        self.page.choose(self.page.locator.NOTES)
        self.page.choose(self.page.locator.REACT)
        self.page.choose(self.page.locator.VEU)
        self.page.choose(self.page.locator.PUBLICK)
        self.page.choose(self.page.locator.CLASSIFIED)
        self.page.choose(self.page.locator.WORDFILE)
