from actions.account.LoginActions import LoginActions
from actions.invoice.InvoiceActions import InvoiceActions
from questions.account.LoginQuestions import LoginQuestions
from questions.invoice.InvoiceQuestions import InvoiceQuestions
from configs.UserConfig import UserConfig

class UserActor:
    def __init__(self, driver):
        self.driver = driver
        self.login_actions = LoginActions(driver)
        self.invoice_actions = InvoiceActions(driver)
        self.login_questions = LoginQuestions(driver)
        self.invoice_questions = InvoiceQuestions(driver)
        self.user_config = UserConfig()

    def login(self, user, is_valid=True):
        self.login_actions.login(user)

    def get_valid_user(self):
        """Returns the valid user credential from the configuration."""
        return self.user_config.get_valid_user()

    def get_invalid_user(self, index):
        """Returns the invalid user credential from the configuration based on the index."""
        return self.user_config.get_invalid_user(index)

    def view_invoice_details(self):
        """Action to view the invoice details."""
        self.invoice_actions.click_first_invoice_details()

    def validate_invoice_details(self, expected_data):
        """Validates invoice details."""
        return self.invoice_questions.validate_invoice_details(expected_data)