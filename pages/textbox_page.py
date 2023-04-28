from selenium.webdriver import ActionChains
from selenium.webdriver.chromium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data.locators import TextBoxLocators


class TextBoxPage(BasePage):


    def __init__(self, driver, wait):
        self.url = "https://demoqa.com/text-box"
        self.locator = TextBoxLocators
        super().__init__(driver, wait)

    def go_to_search_page(self):
        self.go_to_page(self.url)

    def check_title(self, title):
        assert self.get_title() == title

    def make_a_search(self, tb1,tb2,tb3,tb4):
        driver = webdriver.ChromiumDriver
        self.driver.find_element(*self.locator.TB1).send_keys(tb1)
        self.driver.find_element(*self.locator.TB2).send_keys(tb2)
        self.driver.find_element(*self.locator.TB3).send_keys(tb3)
        self.driver.find_element(*self.locator.TB4).send_keys(tb4)
        element=self.driver.find_element(*self.locator.B1)
        action = ActionChains(driver)
        action.move_to_element(element).click()
        tex=self.driver.find_element(*self.locator.RESULTS).text
        if tex=="Name:asdfrfg \n Email:sdfghj@asdfg.com \n Current Address :sdfghyjkihngbfdres \n Permananet Address :asdcfvghyjuik,":
            elem=self.driver.find_element(*self.locator.TB1)
            elem.setText('aaa')
        #assert (self.driver.find_element(*self.locator.RESULTS).text() == "Name:asdfrfg \n Email:sdfghj@asdfg.com \n Current Address :sdfghyjkihngbfdres \n Permananet Address :asdcfvghyjuik,")

        self.driver.save_screenshot("results/results.png")