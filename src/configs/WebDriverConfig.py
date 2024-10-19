import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

class WebDriverConfig:
    def __init__(self):
        self.remote_run = os.getenv("Run", "false").lower() == "true"
        self.browser_choice = os.getenv("Browser", "chrome").lower()
        self.driver = None
        self.create_driver()

    def create_driver(self):
        """Creates a WebDriver instance based on the specified browser."""
        print(f"Remote Run: {self.remote_run}")
        print(f"Browser Choice: {self.browser_choice}")

        chrome_options = ChromeOptions()
        edge_options = EdgeOptions()
        firefox_options = FirefoxOptions()

        self.set_common_options(chrome_options)
        self.set_common_options(edge_options)
        self.set_common_options(firefox_options)

        if self.remote_run:
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--window-position=-2400,-2400")
            edge_options.add_argument("--headless")
            edge_options.add_argument("--window-position=-2400,-2400")
            firefox_options.add_argument("--headless")
            firefox_options.add_argument("--window-position=-2400,-2400")

        if self.browser_choice == "chrome":
            self.driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
        elif self.browser_choice == "edge":
            self.driver = webdriver.Edge(service=EdgeService(), options=edge_options)
        elif self.browser_choice == "firefox":
            self.driver = webdriver.Firefox(service=FirefoxService(), options=firefox_options)
        else:
            raise ValueError(f"Browser not defined: {self.browser_choice}")

    def set_common_options(self, options):
        """Sets common options for the WebDriver."""
        options.add_argument("--disable-gpu")
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-insecure-localhost")

    def quit(self):
        """Closes the WebDriver instance."""
        if self.driver:
            self.driver.quit()