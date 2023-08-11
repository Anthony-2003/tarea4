from selenium.webdriver.common.by import By

class PublicationPage:
    def __init__(self, driver):
        self.driver = driver
        if not "Social network" in self.driver.title:
            raise Exception("This is not the login page")

        self.user_input = (By.ID, "floatingInput")
        self.password_input = (By.ID, "floatingPassword")
        self.login_button = (By.CLASS_NAME, "btn-lg")
        self.btn_publicar = (By.CLASS_NAME, "btn-outline-warning")
        self.textarea = (By.NAME, "Publicacion")
        self.imagen = (By.NAME, "image")
        self.btn_enviar_publicacion = (By.CLASS_NAME, "btn-outline-secondary");

    def type_user_name(self, user):
        self.driver.find_element(*self.user_input).send_keys(user)

    def type_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def click_public_button(self):
        self.driver.find_element(*self.btn_publicar).click()

    def type_caption(self, comment):
        self.driver.find_element(*self.textarea).send_keys(comment)

    def upload_picture(self, picture):
        self.driver.find_element(*self.imagen).send_keys(picture)

    def click_enviar_publicacion (self):
        self.driver.find_element(*self.btn_enviar_publicacion).click()

