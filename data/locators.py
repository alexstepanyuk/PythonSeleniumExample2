from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.XPATH, "//*[@id='search_form_input_homepage']")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='search_button_homepage']")
    RESULTS = (By.XPATH, "//*[@id='links']//*[@data-testid='result']")


class CheckBoxPageLocators:
    HOME = (By.XPATH, '//*[@id="tree-node"]/ol/li/span/button')
    DESKTOP = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]/span/button')
    DOCUMENTS = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/span/button')
    DOWNLOADS = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/span/button')
    WORKSPACE = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/span/button')
    OFFICE = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/span/button')

    NOTES = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]')
    REACT = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[1]/span/label/span[1]')
    VEU = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[3]/span/label/span[1]')
    PUBLICK = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[1]/span/label/span[1]')
    CLASSIFIED = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[3]/span/label/span[1]')
    WORDFILE = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[2]/span/label/span[1]')
