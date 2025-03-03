from selenium.webdriver.common.by import By
import time
from pages.base_page import BasePage


class LoginPage(BasePage):
    Id = (By.ID, "account_id")
    ProceedBtn = (By.XPATH, "//*[text() = \"Proceed\"]")

    UsernameInput = (By.NAME, "username")
    PasswordInput = (By.NAME, "password")
    LoginBtn = (By.XPATH, "//button[contains(text(),'Login')]")
    LoginSuccIndicator = (By.XPATH, "//span[text()= 'shubham.pareek' ]")


    def login1(self, acc_id):
        self.logger.info("Attempting to log in with account ID.")
        self.click(*self.Id)
        self.send_keys(*self.Id, acc_id)
        self.logger.info("logging on learnstage")

        self.click(*self.ProceedBtn)
    

    def login(self, username, password):
        self.click(*self.UsernameInput)
        self.send_keys(*self.UsernameInput, username)
        self.click(*self.PasswordInput)
        self.send_keys(*self.PasswordInput, password)
        self.logger.info("Entered credentials")
        self.click(*self.LoginBtn)

        if self.is_element_present(*self.LoginSuccIndicator):
            self.logger.info("Login successful.")
        else:
            self.logger.warning("Login failed.")
    
