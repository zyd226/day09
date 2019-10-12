# 测试登陆的测试用例
import time
import unittest
from selenium.webdriver.common.by import By
import logging
from page.goods_page import GoodsProxy
from page.home_page import HomeProxy
from utils import DriverUtils


class TestAddCart(unittest.TestCase):
    # 类级别初始化操作
    # 1.获取已经最大化以及设置了隐式等待的浏览器驱动对象
    # 2.需要调用的其他po业务层对象的实例化代码
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtils.get_driver()
        # 因为要调用首页业务层的根据输入关键字搜索商品的方法，所以要实例化该类
        logging.info("-------开始实例化该类首页业务层--------")
        cls.home_proxy = HomeProxy()
        # 因为要调用商品页业务层的将搜索到的商品添加到购物车的方法，所以要实例化该类
        cls.goods_proxy = GoodsProxy()

    # 类级别销毁的操作
    @classmethod
    def tearDownClass(cls):
        DriverUtils.quit_driver()

    # 回归到原点
    # 方法级别fixture
    def setUp(self):
        self.driver.get("http://localhost")

    # 测试用例
    def test_add_cart(self):
        logging.info("-------开始执行搜索商品并添加到购物车的用例--------")
        # 搜索商品并进入详情页面
        self.home_proxy.search_goods("小米")
        # 要在详情页面点击加入购物车
        logging.info("-------调用添加购物车的方法--------")
        self.goods_proxy.add_goods()
        # 获取加入购物车结果
        # 切换iframe窗口
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, "[id*='layui-layer-iframe']"))
        msg = self.driver.find_element(By.CSS_SELECTOR, ".conect-title span").text
        logging.info("-------添加的结果为{}--------".format(msg))
        self.assertEqual("添加成功", msg)
