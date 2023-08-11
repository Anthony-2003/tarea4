import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.LoginPage import LoginPage

import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/login")

    def test_successful_login(self):
        login_page = LoginPage(self.driver)
        time.sleep(2)
        login_page.type_user_name("admin")
        login_page.type_password("1234")
        time.sleep(2)
        login_page.click_login_button()
        time.sleep(2)
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, "test_successful_login.png")
        self.driver.save_screenshot(screenshot_path)

    def test_failed_login(self):
        login_page = LoginPage(self.driver)
        time.sleep(1)
        login_page.type_user_name("andres")
        login_page.type_password("1234")
        time.sleep(1)
        login_page.click_login_button()
        time.sleep(1)
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, "test_failed_login.png")
        self.driver.save_screenshot(screenshot_path)

    def tearDown(self):
        if self.driver:
            # Esperar a que se cargue completamente la página principal antes de cerrar el navegador
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
