class Questions:
    def __init__(self, driver):
        self.driver = driver

    def is_logged_in(self):
        return "/account" in self.driver.current_url

    def is_login_failed(self):
        return "/account" not in self.driver.current_url