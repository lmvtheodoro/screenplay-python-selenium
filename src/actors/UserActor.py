from actions.account.LoginActions import LoginActions
from questions.account.LoginQuestions import LoginQuestions
from configs.UserCredentialsConfig import UserCredentialsConfig

class UserActor:
    def __init__(self, driver):
        self.driver = driver
        self.actions = LoginActions(driver)
        self.questions = LoginQuestions(driver)
        self.user_credentials_config = UserCredentialsConfig()

    def login(self, user, is_valid=True):
        self.actions.login(user)

    def get_valid_user(self):
        """Returns the valid user credential from the configuration."""
        return self.user_credentials_config.get_valid_user()

    def get_invalid_user(self, index):
        """Returns the invalid user credential from the configuration based on the index."""
        return self.user_credentials_config.get_invalid_user(index)