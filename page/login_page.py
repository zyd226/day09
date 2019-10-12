# 登陆页面
# 对象库层
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandler


class LoginPage(BasePage):

    # 1.对象库层初始化方法中将所有需要用到的元素对象都对应定义一个属性，该属性的值为元素对象的定位方式以及值
    # 2.对象库层得完整元素对象查找的工作
    def __init__(self):
        # 获取浏览器驱动
        super().__init__()
        # 用户名输入框
        self.username = (By.ID, 'username')
        # 密码输入框
        self.password = (By.ID, 'password')
        # 验证码输入框
        self.verify_code = (By.ID, 'verify_code')
        # 登陆按钮
        self.submit_btn = (By.NAME, 'sbtbutton')

    # 找用户名输入框
    def find_username(self):
        return self.find_elt(self.username)

    # 找密码输入框
    def find_password(self):
        return self.find_elt(self.password)

    # 找验证码输入框
    def find_verify_code(self):
        return self.find_elt(self.verify_code)

    # 找登陆按钮
    def find_submit_btn(self):
        return self.find_elt(self.submit_btn)


# 操作层
class LoginHandler(BaseHandler):

    # 操作层封装所有元素对应的操作
    def __init__(self):
        self.login_page = LoginPage()

    # 输入用户名
    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    # 输入密码
    def input_password(self, pwd):
        self.input_text(self.login_page.find_password(), pwd)

    # 输入验证码
    def input_code(self, code):
        self.input_text(self.login_page.find_verify_code(), code)

    # 点击登陆按钮
    def click_submit(self):
        self.login_page.find_submit_btn().click()


# 业务层
class LoginProxy:

    # 组织多元素对象的操作，连接起来形成一个功能业务
    def __init__(self):
        self.login_handler = LoginHandler()

    # 登陆操作
    def login(self, username, pwd, code):
        self.login_handler.input_username(username)
        self.login_handler.input_password(pwd)
        self.login_handler.input_code(code)
        self.login_handler.click_submit()
