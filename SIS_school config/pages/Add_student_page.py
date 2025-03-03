from selenium.webdriver.common.by import By
import time
import logging
from pages.base_page import BasePage


class Addstudent(BasePage):
    Sis = (By.XPATH, "//*[text() = \"SIS\"]")
    StIcon = (By.XPATH, '//*[@automation-id="frontend-main_components_sis_MenuItems_FileText"]')
    AddStBtn = (By.XPATH, '//*[@automation-id="frontend-main_src_hocs_RedirectHOC_WrappedComponent"]')
    
    SelectDist = (By.XPATH, "//input[@id='sch_dst_id']")
    SelectSchool = (By.XPATH, "//input[@id='school_realm_name']")
    EmailInput = ()

    def addstudent(self, dist_name, school_name, email):
        self.logger.info("Navigating to SIS.")
        self.click(*self.Sis)
        self.logger.info("Navigated to SIS")
        self.click(*self.StIcon)
        self.click(*self.AddStBtn)
        self.click(*self.SelectDist)
        self.send_keys_in_dropdown(*self.SelectDist, dist_name)
        self.send_keys_in_dropdown(*self.SelectSchool, school_name)
        time.sleep(5)

