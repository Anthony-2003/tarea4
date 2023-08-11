from selenium.webdriver.common.by import By

class EventPage:
    def __init__(self, driver):
        self.driver = driver
        if not "Social network" in self.driver.title:
            raise Exception("This is not the login page")


        self.user_input = (By.ID, "floatingInput")
        self.password_input = (By.ID, "floatingPassword")
        self.login_button = (By.CLASS_NAME, "btn-lg")
        self.crear_evento_btn = (By.CLASS_NAME, "btn-outline-primary")
        self.name_event = (By.NAME, "name")
        self.date_event = (By.NAME, "date")
        self.place_event = (By.NAME, "place")
        self.save_event_btn = (By.CLASS_NAME, "btn-outline-secondary")
        self.my_events_btn = (By.CSS_SELECTOR, 'button[aria-controls="nav-created"]')

    def type_user_name(self, user):
        self.driver.find_element(*self.user_input).send_keys(user)

    def type_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def click_event_button(self):
        self.driver.find_element(*self.crear_evento_btn).click()

    def type_name_event(self, name_event):
        self.driver.find_element(*self.name_event).send_keys(name_event)

    def type_date_event(self, date_event):
        self.driver.find_element(*self.date_event).send_keys(date_event)

    def type_place_event(self, place_event):
        self.driver.find_element(*self.place_event).send_keys(place_event)

    def click_save_event_button(self):
        self.driver.find_element(*self.save_event_btn).click()

    def click_my_events_button(self):
        self.driver.find_element(*self.my_events_btn).click()
