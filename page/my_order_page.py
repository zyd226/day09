# 我的订单
import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandler
from utils import DriverUtils


class MyOrderPage(BasePage):
    def __init__(self):
        super().__init__()
        # 代付款切换tab
        """
        [href*='WAITPAY'][class] 可以直接通过是否包含某个属性来限制元素定位
        """
        self.wait_pay = (By.CSS_SELECTOR, "[href*='WAITPAY'][class]")
        # 立即支付
        self.hurry_pay = (By.CSS_SELECTOR, ".ps_lj")

    # 找到待付款tab
    def find_wait_pay(self):
        return self.find_elt(self.wait_pay)

    # 找立即支付的按钮
    def find_hurry_pay(self):
        return self.find_elt(self.hurry_pay)
    #
    # def find_hrr_pay(self):
    #     return self.driver.find_elements(self.hurry_pay)[0]


class MyOrderHandler(BaseHandler):

    def __init__(self):
        self.my_order_page = MyOrderPage()

    # 点击待付款tab
    def click_wait_pay(self):
        self.my_order_page.find_wait_pay().click()

    # 点击立即支付
    def click_hurry_pay(self):
        self.my_order_page.find_hurry_pay().click()


class MyOrderProxy:
    def __init__(self):
        self.my_order_hanlder = MyOrderHandler()

    # 业务方法:进入我的订单页面-代付款table点击第一个立即付款
    def to_pay_page(self):
        # 切换最新窗口
        time.sleep(3)
        DriverUtils.get_driver().switch_to.window(DriverUtils.get_driver().window_handles[-1])
        # 点击待付款tab
        self.my_order_hanlder.click_wait_pay()
        # 点击立即支付
        self.my_order_hanlder.click_hurry_pay()
