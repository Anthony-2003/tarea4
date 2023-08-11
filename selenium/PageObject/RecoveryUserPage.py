import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.RegisterPage import RegisterPage

import unittest

class RecoveryUserPage(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver
        if not "Social network" in self.driver.title:
            raise Exception("This is not the login page")

        # Definir localizadores para elementos

        self.user_input = (By.ID, "floatingInput")
        self.login_button = (By.CLASS_NAME, "btn-lg")

    def type_name(self, name):
        self.driver.find_element(*self.user_input).send_keys(name)

    def click_restart_button(self):
        self.driver.find_element(*self.login_button).click()



