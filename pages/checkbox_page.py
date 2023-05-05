from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data.locators import CheckBoxPageLocators
from selenium.webdriver.common.by import By


class CheckBoxPage(BasePage):

    def __init__(self, driver, wait):
        self.url = 'https://demoqa.com/checkbox'
        self.locator = CheckBoxPageLocators
        super().__init__(driver, wait)

    def go_to_checkbox_page(self):
        self.go_to_page(self.url)

    def check_title(self, title):
        assert self.get_title() == title

    def save_scr(self, input_text):
        self.driver.save_screenshot("results/checkbox.png")

    def choose(self, name):
        self.driver.find_element(*name).click()
