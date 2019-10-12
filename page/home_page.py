# tpshop 首页
# 对象库层
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandler


class HomePage(BasePage):
    def __init__(self):
        # 获取浏览器驱动
        super().__init__()
        # 登陆超链接
        self.login_link = (By.CSS_SELECTOR, ".red")
        # 搜索输入框
        self.search_box = (By.ID, "q")
        # 搜索按钮
        self.search_btn = (By.CLASS_NAME, "ecsc-search-button")
        # 购物车跳转连接
        self.cart_linK = (By.CSS_SELECTOR, ".c-n")
        # 我的订单
        self.my_order_link = (By.XPATH, "//*[text()='我的订单']")

    def find_login_link(self):
        return self.find_elt(self.login_link)

    # 找搜索输入框元素对象
    def find_search_box(self):
        return self.find_elt(self.search_box)

    # 找搜索按钮元素对象
    def find_search_btn(self):
        return self.find_elt(self.search_btn)

    # 找购物车跳转链接
    def find_cart_link(self):
        return self.find_elt(self.cart_linK)

    # 找我的订单的超链接
    def find_my_order_link(self):
        return self.find_elt(self.my_order_link)


# 操作层
class HomeHandler(BaseHandler):
    def __init__(self):
        self.home_page = HomePage()

    def click_login_link(self):
        self.home_page.find_login_link().click()

    # 搜索输入框输入操作
    def input_search_box(self, key_text):
        self.input_text(self.home_page.find_search_box(), key_text)

    # 搜索按钮的点击操作
    def click_search_btn(self):
        self.home_page.find_search_btn().click()

    # 点击购物车超链接
    def click_cart_link(self):
        self.home_page.find_cart_link().click()

    # 点击我的订单
    def click_my_order_link(self):
        self.home_page.find_my_order_link().click()


# 业务层
class HomeProxy:

    def __init__(self):
        self.home_handler = HomeHandler()

    # 去登陆页面
    def to_login_page(self):
        self.home_handler.click_login_link()

    # 根据输入关键字搜索商品
    def search_goods(self, key_text):
        self.home_handler.input_search_box(key_text)
        self.home_handler.click_search_btn()

    # 去购物车页面
    def to_cart_page(self):
        self.home_handler.click_cart_link()

    # 去我的订单页面
    def to_my_order_page(self):
        self.home_handler.click_my_order_link()
