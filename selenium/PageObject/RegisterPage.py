from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        if not "Social network" in self.driver.title:
            raise Exception("This is not the login page")

        # Definir localizadores para elementos

        self.name = (By.ID, "name")
        self.lastName = (By.ID, "lastname")
        self.userPhone = (By.ID, "phone")
        self.userPicture = (By.CLASS_NAME, "form-control-lg")
        self.userName = (By.ID, "user")
        self.userEmail = (By.ID, "email")
        self.userPassword = (By.ID, "password")
        self.userPasswordConfirm = (By.ID, "confirmpassword")
        self.registerBtn = (By.CLASS_NAME, "btn-lg")

    def type_name(self, name):
        self.driver.find_element(*self.name).send_keys(name)

    def type_last_name(self, last_name):
        self.driver.find_element(*self.lastName).send_keys(last_name)

    def type_user_phone(self, phone):
        self.driver.find_element(*self.userPhone).send_keys(phone)

    def upload_user_picture(self, file_path):
        self.driver.find_element(*self.userPicture).send_keys(file_path)

    def type_user_name(self, user):
        self.driver.find_element(*self.userName).send_keys(user)

    def type_user_email(self, email):
        self.driver.find_element(*self.userEmail).send_keys(email)

    def type_user_password(self, password):
        self.driver.find_element(*self.userPassword).send_keys(password)

    def type_user_password_confirm(self, password):
        self.driver.find_element(*self.userPasswordConfirm).send_keys(password)

    def click_register_button(self):
        self.driver.find_element(*self.registerBtn).click()


