# 包含商品搜索结果页和商品详情页
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class GoodsPage(BasePage):
    def __init__(self):
        # 获取浏览器驱动
        super().__init__()
        # 商品结果信息的元素
        self.goods_link = (By.CSS_SELECTOR, ".xs_img [href*='104']")
        # 商品详情页面加入购物车按钮
        self.join_cart_btn = (By.ID, "join_cart")

    # 找到商品结果信息的元素
    def find_goods_link(self):
        return self.find_elt(self.goods_link)

    # 找到商品详情页面加入购物车按钮
    def find_join_cart_btn(self):
        return self.find_elt(self.join_cart_btn)


class GoodsHandler:

    def __init__(self):
        self.goods_page = GoodsPage()

    # 点击找到商品结果信息的元素
    def click_goods_link(self):
        self.goods_page.find_goods_link().click()

    # 点击商品详情页面加入购物车按钮
    def click_join_cart_btn(self):
        self.goods_page.find_join_cart_btn().click()


class GoodsProxy:

    def __init__(self):
        self.goods_handler = GoodsHandler()

    # 将搜索到的商品添加到购物车
    def add_goods(self):
        # 1.点击搜索到的商品结果(第一个)进入商品详情页面
        self.goods_handler.click_goods_link()
        # 2.在商品详情页面点击加入购物车
        self.goods_handler.click_join_cart_btn()
