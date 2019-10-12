# 测试登陆的测试用例
import unittest
from page.home_page import HomeProxy
from page.my_order_page import MyOrderProxy
from page.pay_page import PayPage
from page.submit_order_page import OrderProxy
from utils import DriverUtils


class TestSubmitOrder(unittest.TestCase):
    # 类级别初始化操作
    # 1.获取已经最大化以及设置了隐式等待的浏览器驱动对象
    # 2.需要调用的其他po业务层对象的实例化代码
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtils.get_driver()
        # 实例化首页业务层对象
        cls.home_proxy = HomeProxy()
        # 实例化购物车和提交订单整合页面业务层对象
        cls.order_proxy = OrderProxy()
        # 实例我的订单页面业务层对象
        cls.my_order_proxy = MyOrderProxy()
        # 实例化支付页面对象
        cls.pay_page = PayPage()

    # 类级别销毁的操作
    @classmethod
    def tearDownClass(cls):
        DriverUtils.quit_driver()

    # 回归到原点
    # 方法级别fixture
    def setUp(self):
        self.driver.get("http://localhost")

    # 提交订单测试用例
    def test_1_subit_order(self):
        # 在首页进入购物车页面
        self.home_proxy.to_cart_page()
        # 点击去结算和提交订单
        msg = self.order_proxy.submission_order()
        # 断言是否提交成功
        self.assertIn("订单提交成功", msg)

    # 订单支付
    def test_2_order_pay(self):
        # 在首页点击我的订单
        self.home_proxy.to_my_order_page()
        # 点击待付款和立即支付按钮
        self.my_order_proxy.to_pay_page()
        # 选择支付方式并确认付款，并且获取返回结果
        msg = self.pay_page.order_pay()
        # 判断支付结果
        self.assertIn('我们将在第一时间给你发货', msg)
