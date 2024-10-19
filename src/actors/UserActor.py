from actions.Actions import Actions
from questions.Questions import Questions
from configs.UserCredentialsConfig import UserCredentialsConfig

class UserActor:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.questions = Questions(driver)
        self.user_credentials_config = UserCredentialsConfig()

    def login(self, user, is_valid=True):
        if is_valid:
            self.actions.login(user)
        else:
            self.actions.login(user)

    def is_logged_in(self):
        return self.questions.is_logged_in()

    def is_login_failed(self):
        return self.questions.is_login_failed()

    def get_valid_user(self):
        """Returns a valid user from the UserCredentialsConfig."""
        return self.user_credentials_config.get_valid_user()

    def get_invalid_user(self, index=0):
        """Returns an invalid user by index from the UserCredentialsConfig."""
        return self.user_credentials_config.get_invalid_user(index)