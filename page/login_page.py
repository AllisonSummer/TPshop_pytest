import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username_edit_text=By.ID,"com.tpshop.malls:id/edit_phone_num"
    password_edit_text =By.ID,"com.tpshop.malls:id/edit_password"
    login_button = By.ID,"com.tpshop.malls:id/btn_login"
    view_pwd_button = By.ID,"com.tpshop.malls:id/img_view_pwd"

    @allure.step(title="输入用户名")
    def input_username(self,text):
        allure.attach("用户名：",text)
        self.input(self.username_edit_text,text)
    @allure.step(title="输入密码")
    def input_password(self,text):
        allure.attach("密码:",text)
        self.input(self.password_edit_text,text)
    @allure.step(title="点击登录")
    def click_login(self):
        self.click(self.login_button)
    @allure.step(title = "点击显示密码")
    def click_view_pwd(self):
        self.click(self.view_pwd_button)

