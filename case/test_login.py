# 测试登陆的测试用例
import json
import time
import unittest

from parameterized import parameterized
from selenium.webdriver.common.by import By
from page.home_page import HomeProxy
from page.login_page import LoginProxy
from utils import DriverUtils
import logging


def build_data():
    login_data = []
    with open("../data/login_data.json", encoding="utf-8")as f:
        test_data = json.load(f)
        for case_data in test_data.values():
            login_data.append((case_data.get("username"),
                               case_data.get("password"),
                               case_data.get("code")))

    return login_data


class TestLogin(unittest.TestCase):
    # 类级别初始化操作
    # 1.获取已经最大化以及设置了隐式等待的浏览器驱动对象
    # 2.需要调用的其他po业务层对象的实例化代码
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtils.get_driver()
        cls.home_proxy = HomeProxy()
        cls.login_proxy = LoginProxy()

    # 类级别销毁的操作
    @classmethod
    def tearDownClass(cls):
        DriverUtils.quit_driver()

    # 方法级别fixture
    def setUp(self):
        self.driver.get("http://localhost")

    # 回归到原点
    # 测试用例
    @parameterized.expand(build_data())
    def test_login(self, username, password, code):
        logging.info("-------开始执行成功登陆的用例--------")
        logging.info("登陆的测试数据为:{} - {}  - {}".format(username, password, code))
        # 点击首页的登陆超链接
        self.home_proxy.to_login_page()
        # 执行登陆操作
        self.login_proxy.login(username, password, code)
        time.sleep(3)
        # 断言
        try:
            self.assertTrue(self.driver.find_element(By.XPATH, "//*[text()='安全退出']"))
        except Exception as e:
            self.assertTrue(False)
            raise e
