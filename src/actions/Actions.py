from configs.UrlManagerConfig import UrlManagerConfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Actions:
    def __init__(self, driver):
        self.driver = driver

    def login(self, user):
        url_manager = UrlManagerConfig()
        self.driver.get(url_manager.base_url)

        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )

        username_field.send_keys(user.username)
        password_field.send_keys(user.password)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnLogin"))
        )
        login_button.click()