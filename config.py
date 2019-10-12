import logging.handlers
import os

# 获取当前文件所在路径
# path = os.path.abspath(os.path.dirname("__file__"))
# path = os.getcwd()


# 日志配置方法
def basic_logger():
    # 创建日志器
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    # 创建处理器
    lht = logging.handlers.TimedRotatingFileHandler(filename="../log/a.log", when="midnight", interval=1, backupCount=2)
    ls = logging.StreamHandler()
    # 创建格式化器
    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 将格式化器添加到处理器
    lht.setFormatter(formatter)
    ls.setFormatter(formatter)
    # 将处理器添加日志器
    logger.addHandler(lht)
    logger.addHandler(ls)
