from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data.locators import *
from time import sleep

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
        self.driver.find_element(*self.locator.YES_TEXT).click()
        sleep(1)
        res = self.driver.find_element(*self.locator.RESULTS).text
        assert res == "Yes"

    def check_imp_radio(self):
        self.driver.find_element(*self.locator.IMP_TEXT).click()
        sleep(1)
        res = self.driver.find_element(*self.locator.RESULTS).text
        assert res == "Impressive"

    def check_no_radio(self):
        self.driver.find_element(*self.locator.NO_TEXT).click()
        sleep(1)
        try:
            res = self.driver.find_element(*self.locator.RESULTS).text
            if res == "Impressive" or res == "Yes" or res == "No":
                raise
        except:
            assert True
        else:
            assert False

    def make_a_search(self, input_text):
        self.driver.find_element(*self.locator.SEARCH_INPUT).send_keys(input_text)
        self.driver.find_element(*self.locator.SEARCH_BUTTON).click()
        self.wait.until(EC.presence_of_element_located(self.locator.RESULTS))
        self.driver.save_screenshot("results/results.png")