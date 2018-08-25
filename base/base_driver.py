from appium import webdriver


def init_driver():
    desired_caps = dict()
    # 设备信息
    desired_caps["platformName"] = "Android"
    desired_caps["platformVersion"] = "5.1"
    desired_caps["deviceName"] = '192.168.56.101:5555'

    # app信息
    desired_caps["appPackage"] ="com.tpshop.malls"
    desired_caps["appActivity"]=".SPMainActivity"

    # 解决输入中文
    desired_caps["unicodeKeyboard"] =True
    desired_caps["resetKeyboard"] = True

    # 欢迎界面
    # desired_caps["noReset"] = True

    # toast
    desired_caps["automationName"] = "Uiautomator2"

    # 声明我们的driver对象
    return webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
