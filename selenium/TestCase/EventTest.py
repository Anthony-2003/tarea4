import os
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.EventPage import EventPage
from PageObject.LoginPage import LoginPage

import unittest

class EventTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/login")

    def create_event_succesfully(self):
        event_page = EventPage(self.driver)
        time.sleep(2)
        event_page.type_user_name("admin")
        event_page.type_password("1234")
        event_page.click_login_button()
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        event_item = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/events"]')))
        time.sleep(2)
        event_item.click()
        time.sleep(2)
        event_page.click_event_button()
        time.sleep(2)
        event_page.type_name_event("Concierto musical")
        event_page.type_date_event("2023-08-13T15:43")
        event_page.type_place_event("Estadio Quisqueya")
        event_page.click_save_event_button()
        time.sleep(2)
        event_page.click_my_events_button()
        time.sleep(2)

        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, "test_succesfully_event.png")
        self.driver.save_screenshot(screenshot_path)

    def create_event_failed(self):
        event_page = EventPage(self.driver)
        event_page.type_user_name("admin")
        event_page.type_password("1234")
        event_page.click_login_button()

        wait = WebDriverWait(self.driver, 10)
        event_item = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/events"]')))

        event_item.click()

        event_page.click_event_button()

        event_page.type_name_event("")
        event_page.type_date_event("2023-08-11T21:22")
        event_page.type_place_event("Estadio Quisqueya")

        event_page.click_save_event_button()
        time.sleep(2)

        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, "test_failed_event.png")
        self.driver.save_screenshot(screenshot_path)

    def create_event_past_date(self):
        event_page = EventPage(self.driver)
        event_page.type_user_name("admin")
        event_page.type_password("1234")
        event_page.click_login_button()

        wait = WebDriverWait(self.driver, 10)
        event_item = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/events"]')))

        event_item.click()

        event_page.click_event_button()

        event_page.type_name_event("Concierto")
        event_page.type_date_event("2022-08-11T21:22")
        event_page.type_place_event("Estadio Quisqueya")

        event_page.click_save_event_button()
        time.sleep(2)

        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, "test_past_date_event.png")
        self.driver.save_screenshot(screenshot_path)


def tearDown(self):
    if self.driver:
        # Esperar a que se cargue completamente la página principal antes de cerrar el navegador
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
