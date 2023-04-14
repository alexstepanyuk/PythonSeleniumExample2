from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.XPATH, "//*[@id='search_form_input_homepage']")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='search_button_homepage']")
    RESULTS = (By.XPATH, "//*[@id='links']//*[@data-testid='result']")


class DemoqaRadioButtonPageLocators:

    RESULTS = (By.XPATH, "//*[@class='text-success']")

    YES_DIV = (By.XPATH, "//*[@id='yesRadio']/..")
    YES_RADIO = (By.XPATH, "//*[@id='yesRadio']")

    IMPRESSIVE_RADIO = (By.XPATH, "//*[@id='impressiveRadio']")
    NO_RADIO = (By.XPATH, "//*[@id='noRadio']")