from configs.UrlManagerConfig import UrlManagerConfig
from interactions.Interactions import Interactions
from selenium.webdriver.common.by import By

class LoginActions:
    def __init__(self, driver):
        self.driver = driver
        self.interactions = Interactions(driver)

    def navigate_to_login_page(self):
        url_manager = UrlManagerConfig()
        self.driver.get(url_manager.base_url)

    def enter_credentials(self, user):
        self.interactions.enter_text((By.NAME, "username"), user.username)
        self.interactions.enter_text((By.NAME, "password"), user.password)

    def click_login(self):
        self.interactions.click((By.ID, "btnLogin"))

    def login(self, user):
        self.navigate_to_login_page()
        self.enter_credentials(user)
        self.click_login()