#from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data.locators import DemoqaRadioButtonPageLocators
from time import sleep

class DemoqaRadioButtonPage(BasePage):

    def __init__(self, driver, wait):
        self.url = "https://demoqa.com/radio-button"
        self.locator = DemoqaRadioButtonPageLocators
        super().__init__(driver, wait)

    def go_to_search_page(self):
        self.go_to_page(self.url)

    def check_yes_radio(self):
        self.driver.find_element(*self.locator.YES_TEXT).click()
        sleep(1)
        res = self.driver.find_element(*self.locator.RESULTS).text
        assert self.driver.find_element(*self.locator.YES_RADIO).is_selected() and res == "Yes"

    def check_imp_radio(self):
        self.driver.find_element(*self.locator.IMP_TEXT).click()
        sleep(1)
        res = self.driver.find_element(*self.locator.RESULTS).text
        assert self.driver.find_element(*self.locator.IMP_RADIO).is_selected() and res == "Impressive"

    def check_no_radio(self):
        self.driver.find_element(*self.locator.NO_TEXT).click()
        sleep(1)
        assert not self.driver.find_element(*self.locator.NO_RADIO).is_selected()