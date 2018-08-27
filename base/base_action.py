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

    # 时间的频率设置的小一点，否则他就过去了你找不到,这个方法含义是传一个toast上部分的值，能得到toast上完整的值
    def find_toast(self,message,timeout=3.0,poll=0.1):
        mes = "//*[contains(@text,'"+message+"')]"
        element = WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(By.XPATH,mes))
        return element.text

    def is_toast_exist(self,message):
        try:
            self.find_toast(message)
            return True
        except Exception:
            return False

    def is_location_exit(self,location):
        try:
            self.find_element(location)
            return True
        except Exception:
            return False
