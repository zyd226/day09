# 基类
# 对象库层的基类
# 参数抽取原则：
# 1.作为基类，是方法提供方，需要明确需要的类容(可以是对象、列表、字符串、数字)
# 2.作为子类，是方法调用方，需要明确能给的类容(可以是对象、列表、字符串、数字)
# 3.两方供需对应匹配上后，就可以当成参数进行传递。
from utils import DriverUtils


class BasePage:

    def __init__(self):
        self.driver = DriverUtils.get_driver()

    # 封装元素定位的方法
    def find_elt(self, location):
        return self.driver.find_element(*location)


# 操作层的基类
class BaseHandler:
    # 封装元素信息输入的方法,需要知道到底是哪个元素对应要执行输入
    def input_text(self, element, username):
        element.clear()
        element.send_keys(username)
