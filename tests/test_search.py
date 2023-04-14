# coding=utf-8
import pytest
from pages.search_page import *
from tests.base_test import BaseTest


# class TestSearch(BaseTest):
#
#     @pytest.fixture
#     def load_pages(self):
#         self.page = SearchPage(self.driver, self.wait)
#         self.page.go_to_search_page()
#
#     def test_title(self, load_pages):
#         self.page.check_title("DuckDuckGo — Максимум конфиденциальности, минимум усилий.")
#
#     def test_search(self, load_pages):
#         self.page.make_a_search("Selenium")

class TestDemoqaRadioButton(BaseTest):

    @pytest.fixture
    def load_pages(self):
        self.page = DemoqaRadioButtonPage(self.driver, self.wait)
        self.page.go_to_search_page()

    def test_radios(self, load_pages):
        self.page.check_yes_radio()

    # def test_search(self, load_pages):
    #     self.page.make_a_search("Selenium")
