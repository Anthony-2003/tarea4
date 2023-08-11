import unittest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from TestCase.loginTest import TestLogin

class TestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def test_successful_login(self):
        test_login = TestLogin(self.driver)
        test_login.setUp()
        test_login.test_successful_login()
        test_login.tearDown()

    def test_failed_login(self):
        test_login = TestLogin(self.driver)
        test_login.setUp()
        test_login.test_failed_login()
        test_login.tearDown()

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
