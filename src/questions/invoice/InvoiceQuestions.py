from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InvoiceQuestions:
    def __init__(self, driver):
        self.driver = driver
    
    def validate_invoice_details(self, expected_data):
        """Validate the invoice details on the page against the expected data."""
        wait = WebDriverWait(self.driver, 10)

        actual_data = {
            "HotelName": wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h4.mt-5"))).text,
            "InvoiceDate": wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Invoice Date:']/parent::li"))).get_attribute('innerText').split(":")[1].strip(),
            "DueDate": wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Due Date:']/parent::li"))).get_attribute('innerText').split(":")[1].strip(),
            "InvoiceNumber": wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h6.mt-2"))).text.split("#")[1].strip().split()[0],
            "BookingCode": wait.until(EC.visibility_of_element_located((By.XPATH, "//td[text()='Booking Code']/following-sibling::td"))).text,
            "CustomerDetails": wait.until(EC.visibility_of_element_located((By.XPATH, "//h5[text()='Customer Details']/following-sibling::div"))).get_attribute('innerText').replace("\n", " ").strip(),
            "Room": wait.until(EC.visibility_of_element_located((By.XPATH, "//td[text()='Room']/following-sibling::td"))).text,
            "CheckIn": wait.until(EC.visibility_of_element_located((By.XPATH, "//td[contains(text(),'Check-In')]/following-sibling::td"))).text,
            "CheckOut": wait.until(EC.visibility_of_element_located((By.XPATH, "//td[text()='Check-Out']/following-sibling::td"))).text,
            "TotalStayCount": int(wait.until(EC.visibility_of_element_located((By.XPATH, "//td[text()='Total Stay Count']/following-sibling::td"))).text),
            "TotalStayAmount": wait.until(EC.visibility_of_element_located((By.XPATH, "//td[text()='Total Stay Amount']/following-sibling::td"))).text,
            "DepositNow": wait.until(EC.visibility_of_element_located((By.XPATH, "//h5[text()='Billing Details']/following-sibling::table/tbody/tr/td[1]"))).text.strip(),
            "TaxVAT": wait.until(EC.visibility_of_element_located((By.XPATH, "//h5[text()='Billing Details']/following-sibling::table/tbody/tr/td[2]"))).text.strip(),
            "TotalAmount": wait.until(EC.visibility_of_element_located((By.XPATH, "//h5[text()='Billing Details']/following-sibling::table/tbody/tr/td[3]"))).text.strip()
        }

        # Validate actual data against expected data
        for key, value in expected_data.items():
            if actual_data[key] != value:
                print(f"Validation failed for {key}: Expected {value}, but got {actual_data[key]}")
                return False

        print("All invoice details validated successfully!")
        return True