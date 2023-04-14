from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data.locators import *


class SearchPage(BasePage):

    def __init__(self, driver, wait):
        self.url = "https://duckduckgo.com/"
        self.locator = SearchPageLocators
        super().__init__(driver, wait)

    def go_to_search_page(self):
        self.go_to_page(self.url)

    def check_title(self, title):
        assert self.get_title() == title

    def make_a_search(self, input_text):
        self.driver.find_element(*self.locator.SEARCH_INPUT).send_keys(input_text)
        self.driver.find_element(*self.locator.SEARCH_BUTTON).click()
        self.wait.until(EC.presence_of_element_located(self.locator.RESULTS))
        self.driver.save_screenshot("results/results.png")


class DemoqaRadioButtonPage(BasePage):

    def __init__(self, driver, wait):
        self.url = "https://demoqa.com/radio-button"
        self.locator = DemoqaRadioButtonPageLocators
        super().__init__(driver, wait)

    def go_to_search_page(self):
        self.go_to_page(self.url)

    def check_title(self, title):
        assert self.get_title() == title

    def check_yes_radio(self):
        yes_div =  self.driver.find_element(*self.locator.YES_DIV)
        self.driver.execute_script("arguments[0].click();", yes_div)
        self.wait.until(EC.presence_of_element_located(self.locator.RESULTS))
        assert (self.driver.find_element(*self.locator.RESULTS).text() == "Yes")



    def make_a_search(self, input_text):
        self.driver.find_element(*self.locator.SEARCH_INPUT).send_keys(input_text)
        self.driver.find_element(*self.locator.SEARCH_BUTTON).click()
        self.wait.until(EC.presence_of_element_located(self.locator.RESULTS))
        self.driver.save_screenshot("results/results.png")