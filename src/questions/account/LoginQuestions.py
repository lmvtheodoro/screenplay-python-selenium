from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginQuestions:
    def __init__(self, driver):
        self.driver = driver

    def is_logged_in(self):
        return "/account" in self.driver.current_url

    def is_login_failed(self):
        return "/account" not in self.driver.current_url

    def what_is_login_error_message(self):
        """Returns the error message if displayed."""
        try:
            error_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger"))
            )
            return error_element.text
        except Exception:
            return None