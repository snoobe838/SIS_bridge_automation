import sys
import os
import time
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from selenium import webdriver

from tests.test_login import test_valid_login
from tests.test_add_student import test_add_student

def main():
    driver = webdriver.Chrome()
    
    test_valid_login(driver)
        
    test_add_student(driver)
    
if __name__ == "__main__":
    main()