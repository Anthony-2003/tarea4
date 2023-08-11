import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.RegisterPage import RegisterPage

import unittest

class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/login")

    def test_successful_register(self):
        register_page = RegisterPage(self.driver)

        time.sleep(2)

        wait = WebDriverWait(self.driver, 10)
        register_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/signup"]')))

        # Hacer clic en el enlace
        register_link.click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))  # Cambia el identificador a uno presente en la nueva página
        )
        time.sleep(2)
        # Llamar al método correcto

        register_page.type_name("Ricky")

        register_page.type_last_name("Henrique")

        register_page.type_user_phone("(829)-317-3061")

        register_page.upload_user_picture("C:/Users/ANTHO-PC/Desktop/Folder/Carpetas/PERFIL.jpg")

        register_page.type_user_name("testdejeemplo3")

        register_page.type_user_email("jesustaverazdias99@gmail.com")

        register_page.type_user_password("123456789")

        register_page.type_user_password_confirm("123456789")

        time.sleep(2)
        register_page.click_register_button()  # Llamar al método correcto

        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, "test_successful_register.png")
        self.driver.save_screenshot(screenshot_path)

    def test_empty_field (self):
        register_page = RegisterPage(self.driver)

        wait = WebDriverWait(self.driver, 10)
        register_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/signup"]')))

        time.sleep(2)
        # Hacer clic en el enlace
        register_link.click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))  # Cambia el identificador a uno presente en la nueva página
        )

        time.sleep(2)
        register_page.type_name("")
        register_page.type_last_name("Henrique")
        register_page.type_user_phone("(829)-317-3061")
        register_page.upload_user_picture("C:/Users/ANTHO-PC/Desktop/Folder/Carpetas/PERFIL.jpg")
        register_page.type_user_name("minombredeusuario")
        register_page.type_user_email("jesustaverazdias2323@gmail.com")
        register_page.type_user_password("123456789")
        register_page.type_user_password_confirm("123456789")
        register_page.click_register_button()  # Llamar al método correcto
        time.sleep(2)
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, "test_empty_register.png")
        self.driver.save_screenshot(screenshot_path)

    def test_same_user(self):
            register_page = RegisterPage(self.driver)

            wait = WebDriverWait(self.driver, 10)
            register_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/signup"]')))

            # Hacer clic en el enlace
            register_link.click()

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "name"))
                # Cambia el identificador a uno presente en la nueva página
            )

            register_page.type_name("jonas")
            register_page.type_last_name("Henrique")
            register_page.type_user_phone("(829)-317-3061")
            register_page.upload_user_picture("C:/Users/ANTHO-PC/Desktop/Folder/Carpetas/PERFIL.jpg")
            register_page.type_user_name("minombredeusuario")
            register_page.type_user_email("jesustaverazdias2323@gmail.com")
            register_page.type_user_password("123456789")
            register_page.type_user_password_confirm("123456789")
            register_page.click_register_button()  # Llamar al método correcto
            time.sleep(2)
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            screenshot_path = os.path.join(screenshot_dir, "test_same_user_register.png")
            self.driver.save_screenshot(screenshot_path)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
