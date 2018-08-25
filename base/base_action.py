from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    # def find_element(self,location):
    #     return self.driver.find_element(location[0],location[1])

    def find_element(self, location, timeout=10.0, poll=1.0):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(location[0], location[1]))
    def find_elements(self, location, timeout=10.0, poll=1.0):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(location[0], location[1]))

    def click(self,location):
        self.find_element(location).click()
    def input(self,location,text):
        self.find_element(location).send_keys(text)



