from selenium.webdriver.common.by import By
import time
from pages.base_page import BasePage


class Addstudent(BasePage):
    Sis = (By.XPATH, "//*[text() = \"SIS\"]")
    StIcon = (By.XPATH, '//*[@automation-id="frontend-main_components_sis_MenuItems_FileText"]')
    AddStBtn = (By.XPATH, '//*[@automation-id="frontend-main_src_hocs_RedirectHOC_WrappedComponent"]')
    
    SelectDist = (By.XPATH, "//input[@id='sch_dst_id']")
    SelectSchool = (By.XPATH, "//input[@id='school_realm_name']")
    EnterEmail = (By.ID, "email")
    EnterPass = (By.ID, "password")
    EnterConfPass = (By.ID, "confirmPassword")
    EnterFname = (By.ID, "first_name")
    EnterLname = (By.ID, "last_name")
    EnterDob = (By.ID, "dob")
    SelectGender = (By.ID, "gender")
    SelectEthnicity = (By.ID, "ethnicity")

    EmailInput = ()

    def addstudent(self, dist_name, school_name, email, password, confirmpassword, firstname, lastname, dob, gender, ethnicity):
        self.logger.info("Navigating to SIS.")
        self.click(*self.Sis)
        self.logger.info("Navigated to SIS")
        self.click(*self.StIcon)
        self.click(*self.AddStBtn)
        self.click(*self.SelectDist)
        self.send_keys_in_dropdown(*self.SelectDist, dist_name)
        self.send_keys_in_dropdown(*self.SelectSchool, school_name)
        self.send_keys(*self.EnterEmail, email)
        self.send_keys(*self.EnterPass, password)
        self.send_keys(*self.EnterConfPass, confirmpassword)
        self.send_keys(*self.EnterFname, firstname)
        self.send_keys(*self.EnterLname, lastname)
        self.send_keys(*self.EnterDob, dob)
        self.select_dropdown_by_visible_text(*self.SelectGender, gender)
        self.select_dropdown_by_visible_text(*self.SelectEthnicity, ethnicity)
        time.sleep(5)

