# 1.导包
import time

from case.test_add_cart import TestAddCart
from case.test_login import TestLogin
from case.test_order import TestSubmitOrder
from lib.HTMLTestRunner import HTMLTestRunner
import unittest

from utils import DriverUtils

# 把关闭浏览器开关给关闭
DriverUtils.open_key(False)

# 2.组织测试套件(添加测试用例)
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestAddCart))
suite.addTest(unittest.makeSuite(TestSubmitOrder))

# # 实例化测试运行器
# runner = unittest.TextTestRunner()
# runner.run(suite)
# # 3.定义测试报告路径
report_path = "../report/test_{}.html".format(time.strftime("%Y%m%d%H%M%S"))
# 4.打开测试报告文件
with open(report_path, 'wb')as f:
    # 5.实例化HTMLTestRunner
    runner = HTMLTestRunner(f, title="测试报告", description="Chrome")
    # 6.执行测试套件
    runner.run(suite)

# 把关浏览器开关给打开，然后再主动调用一次关闭浏览器对象的方法
DriverUtils.open_key(True)
DriverUtils.quit_driver()
