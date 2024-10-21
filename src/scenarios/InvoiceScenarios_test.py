from configs.WebDriverConfig import WebDriverConfig
from actors.UserActor import UserActor

class TestInvoiceScenarios:
    
    def setup_method(self):
        self.driver_config = WebDriverConfig()
        self.driver = self.driver_config.driver  
        self.user_actor = UserActor(self.driver)

        self.expected_invoice_data = self.user_actor.user_config.load_invoice()

        self.driver.delete_all_cookies()

    def teardown_method(self):
        self.driver.quit()
    
    def test_invoice_details(self):
        valid_user = self.user_actor.get_valid_user()
        self.user_actor.login(valid_user)
        assert self.user_actor.login_questions.is_logged_in(), "Expected to be logged in with valid user"
        
        self.user_actor.view_invoice_details()

        assert self.user_actor.validate_invoice_details(self.expected_invoice_data), "Invoice details validation failed"