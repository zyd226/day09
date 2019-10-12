# 支付页面
import time

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utils import DriverUtils


class PayPage(BasePage):

    def __init__(self):
        super().__init__()
        # 货到付款选项
        self.cash_delivery = (By.CSS_SELECTOR, "[value='pay_code=cod']")
        # 确认支付按钮
        self.confirm_pay = (By.CSS_SELECTOR, ".button-confirm-payment")

    # 确认支付业务操作方法
    def order_pay(self):
        # 窗口切换
        time.sleep(3)
        DriverUtils.get_driver().switch_to.window(DriverUtils.get_driver().window_handles[-1])
        # 勾选货到付款
        self.find_elt(self.cash_delivery).click()
        # 点击确认支付按钮
        self.find_elt(self.confirm_pay).click()
        time.sleep(3)
        # 获取实际支付结果信息
        return self.find_elt((By.CSS_SELECTOR, '.erhuh h3')).text
