from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        if not "Social network" in self.driver.title:
            raise Exception("This is not the login page")

        self.user_input = (By.ID, "floatingInput")
        self.password_input = (By.ID, "floatingPassword")
        self.login_button = (By.CLASS_NAME, "btn-lg")

    def type_user_name(self, user):
        self.driver.find_element(*self.user_input).send_keys(user)

    def type_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()
