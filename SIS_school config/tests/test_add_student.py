import sys
import os
import time
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.Add_student_page import Addstudent

def test_add_student(driver):
    Add_student_page = Addstudent(driver)
    Add_student_page.addstudent("_One_8", "A Godlike School", "")
        