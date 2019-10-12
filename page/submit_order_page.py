# 购物车页面、提交订单页面
# 对象库层

# 什么时候才整合页面：
# 1.当测试用例经过某个页面时，只操作的一个或者很少量的元素对象，重新封装一个新的PO对应py文件，不能节省较多的代码时
# 2.其他用例也不会操作该页面的其他元素

import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utils import DriverUtils


class OrderPage(BasePage):

    def __init__(self):
        super().__init__()
        # 去结算按钮
        self.settlement_btn = (By.CSS_SELECTOR, ".gwc-qjs")
        # 提交订单按钮
        self.submit_order_btn = (By.CSS_SELECTOR, ".Sub-orders")

    # 找到去结算按钮的元素对象
    def find_settlement_btn(self):
        return self.find_elt(self.settlement_btn)

    # 找到提交订单按钮的元素对象
    def find_submit_order_btn(self):
        return self.find_elt(self.submit_order_btn)


# 操作层
class OrderHandler:

    def __init__(self):
        self.order_page = OrderPage()

    # 点击去结算按钮
    def click_settlement_btn(self):
        self.order_page.find_settlement_btn().click()

    # 点击提交订单按钮
    def click_submit_order_btn(self):
        self.order_page.find_submit_order_btn().click()


# 业务层
class OrderProxy:

    def __init__(self):
        self.order_handler = OrderHandler()

    # 提交订单并且返回提交订单结果
    def submission_order(self):
        # 点击去结算
        self.order_handler.click_settlement_btn()
        # 提交订单
        time.sleep(3)
        self.order_handler.click_submit_order_btn()
        # 获取提交订单结果并返回结果信息
        msg = DriverUtils.get_driver().find_element(By.CSS_SELECTOR, ".erhuh h3").text
        return msg
