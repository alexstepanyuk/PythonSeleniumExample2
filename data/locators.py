from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.XPATH, "//*[@id='search_form_input_homepage']")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='search_button_homepage']")
    RESULTS = (By.XPATH, "//*[@id='links']//*[@data-testid='result']")

class TextBoxLocators:
    TB1 = (By.XPATH, "//*[@id='userName']")
    TB2 = (By.XPATH, "//*[@id='userEmail']")
    TB3 = (By.XPATH, "//*[@id='currentAddress']")
    TB4 = (By.XPATH, "//*[@id='permanentAddress']")
    B1 = (By.XPATH, "//*[@id='submit']")
    RESULTS = (By.XPATH, '//*[@id="output"]/div')
