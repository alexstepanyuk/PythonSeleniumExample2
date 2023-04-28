import pytest
from pages.demoqa_radio_button_page import DemoqaRadioButtonPage
from tests.base_test import BaseTest

class TestDemoqaRadioButton(BaseTest):
    @pytest.fixture
    def load_pages(self):
        self.page = DemoqaRadioButtonPage(self.driver, self.wait)
        self.page.go_to_search_page()

    def test_radios(self, load_pages):
        self.page.check_yes_radio()
        self.page.check_imp_radio()
        self.page.check_no_radio()
