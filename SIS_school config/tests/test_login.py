import sys
import os
import time
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.login_page import LoginPage

def test_valid_login(driver):
        driver.get("https://sis-admin.stpldevs.com/sis/login")
        login_page = LoginPage(driver)
        login_page.login1("learnstageqa")
        login_page.login("shubham.pareek", "User@1234")
