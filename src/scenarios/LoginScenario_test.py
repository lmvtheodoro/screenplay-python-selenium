import pytest
from configs.WebDriverConfig import WebDriverConfig
from actors.UserActor import UserActor
from configs.UserCredentialsConfig import UserCredentialsConfig

class TestLoginScenario:
    
    def setup_method(self):
        self.driver_config = WebDriverConfig()
        self.driver = self.driver_config.driver  
        self.user_actor = UserActor(self.driver)

        self.driver.delete_all_cookies()
        
    def teardown_method(self):
        self.driver.quit()
    
    def test_valid_login(self):
        valid_user = self.user_actor.get_valid_user()
        self.user_actor.login(valid_user)
        assert self.user_actor.questions.is_logged_in(), "Expected to be logged in with valid user"

    @pytest.mark.parametrize("index", range(4))
    def test_invalid_login(self, index):
        invalid_user = self.user_actor.get_invalid_user(index)
        
        print(f"Testing login with invalid user: {invalid_user}")

        self.user_actor.login(invalid_user)

        assert self.user_actor.questions.is_login_failed(), "Expected login to fail for invalid user"
        
        expected_error_message = "Wrong username or password."
        actual_error_message = self.user_actor.questions.what_is_login_error_message()
        assert actual_error_message == expected_error_message, f"Expected error message '{expected_error_message}', but got '{actual_error_message}'"