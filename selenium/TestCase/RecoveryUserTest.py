import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.RecoveryUserPage import RecoveryUserPage
from PageObject.RegisterPage import RegisterPage

class RecoveryUserTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/login")  # add assertion here

    def test_successful_recovery(self):
            recovery_page = RecoveryUserPage(self.driver)

            wait = WebDriverWait(self.driver, 10)
            register_link = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-link')))

            time.sleep(2)
            # Hacer clic en el enlace
            register_link.click()

            # Llamar al método correcto

            recovery_page.type_name("master")
            time.sleep(2)
            recovery_page.click_restart_button()
            time.sleep(2)
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            screenshot_path = os.path.join(screenshot_dir, "test_successful_recovery_user.png")
            self.driver.save_screenshot(screenshot_path)

    def test_failed_recovery(self):
            recovery_page = RecoveryUserPage(self.driver)

            wait = WebDriverWait(self.driver, 10)
            register_link = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-link')))

            time.sleep(2)
            # Hacer clic en el enlace
            register_link.click()

            # Llamar al método correcto

            recovery_page.type_name("no existo")
            time.sleep(2)
            recovery_page.click_restart_button()
            time.sleep(2)

            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            screenshot_path = os.path.join(screenshot_dir, "test_failed_recovery_user.png")
            self.driver.save_screenshot(screenshot_path)

if __name__ == '__main__':
    unittest.main()
