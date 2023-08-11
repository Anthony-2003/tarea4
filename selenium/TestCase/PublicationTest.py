import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.LoginPage import LoginPage

import unittest

from PageObject.PublicationPage import PublicationPage


class PublicationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/login")

    def test_publication_succesfully(self):
        publication_page = PublicationPage(self.driver)
        publication_page.type_user_name("admin")
        publication_page.type_password("1234")
        publication_page.click_login_button()
        time.sleep(2)
        publication_page.click_public_button()
        time.sleep(2)
        publication_page.type_caption("Esto es una prueba de un test")
        publication_page.upload_picture("C:/Users/ANTHO-PC/Desktop/Folder/Carpetas/PERFIL.jpg")
        time.sleep(2)
        publication_page.click_enviar_publicacion()
        time.sleep(2)

        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, "test_publication_succesfully.png")
        self.driver.save_screenshot(screenshot_path)

    def test_publication_failed(self):
        publication_page = PublicationPage(self.driver)
        publication_page.type_user_name("admin")
        publication_page.type_password("1234")
        publication_page.click_login_button()
        time.sleep(2)
        publication_page.click_public_button()
        time.sleep(2)
        publication_page.click_enviar_publicacion()
        time.sleep(2)

        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, "test_publication_failed.png")
        self.driver.save_screenshot(screenshot_path)

def tearDown(self):
    if self.driver:
        # Esperar a que se cargue completamente la página principal antes de cerrar el navegador
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
