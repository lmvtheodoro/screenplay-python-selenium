import pytest
from configs.WebDriverConfig import WebDriverConfig
from actors.UserActor import UserActor
from configs.UserCredentialsConfig import UserCredentialsConfig

class TestLoginScenario:
    
    def setup_method(self):
        self.driver_config = WebDriverConfig()
        self.user_credentials_config = UserCredentialsConfig()
        self.driver = self.driver_config.driver  
        self.user_actor = UserActor(self.driver)

        self.driver.delete_all_cookies()
        
    def teardown_method(self):
        self.driver.quit()
    
    def test_valid_login(self):
        valid_user = self.user_actor.get_valid_user()
        self.user_actor.login(valid_user)
        assert self.user_actor.is_logged_in()

    @pytest.mark.parametrize("index", range(4))
    def test_invalid_login(self, index):
        invalid_user = self.user_actor.get_invalid_user(index)
        
        print(f"Testing login with invalid user: {invalid_user.username}")

        self.user_actor.login(invalid_user, is_valid=False)
        assert self.user_actor.is_login_failed()