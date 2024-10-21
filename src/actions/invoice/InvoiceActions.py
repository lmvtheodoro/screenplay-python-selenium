from interactions.Interactions import Interactions
from selenium.webdriver.common.by import By

class InvoiceActions:
    def __init__(self, driver):
        self.driver = driver
        self.interactions = Interactions(driver)

    def click_first_invoice_details(self):
        """
        Action to click the Invoice Details link for the first item presented on the screen.
        """
        locator = (By.CSS_SELECTOR, "a[href='/invoice/0']")

        # Force the link to open in the same tab
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].setAttribute('target', '_self');", element)
        
        self.interactions.click(locator)