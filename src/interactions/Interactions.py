from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Interactions:
    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        element.send_keys(text)

    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()