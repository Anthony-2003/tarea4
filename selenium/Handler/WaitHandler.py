from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait


class WaitHandler:
    @staticmethod
    def element_is_present(driver, locator):
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located(locator))
            return True
        except:
            return False
