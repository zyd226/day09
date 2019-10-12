# 存放的是一个公用的工具类
# 浏览器驱动对象获取和关闭的工具类
from selenium import webdriver


class DriverUtils:
    __driver = None

    __openKey = True

    # 获取浏览器驱动对象
    # 1.为了方便调用，将该方法配置成类级别的方法
    # 2.为了保障浏览器驱动在整个测试过程中的唯一性，加上判断当前是否以有浏览器驱动的存在
    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(10)
        return cls.__driver

    # 关闭浏览器驱动对象
    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None and cls.__openKey is True:
            cls.get_driver().quit()
            cls.__driver = None

    # 关闭浏览器驱动开关
    @classmethod
    def open_key(cls, is_open):
        cls.__openKey = is_open
