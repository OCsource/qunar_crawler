import logging

# 用于获取logger对象
# 参数：类型0 或 非0
# 返回：相应的logger对象
def getLogger(type=0):
    # 用于记录DB出错的提及
    # 创建一个logger
    logger = logging.getLogger("consoleLog")
    logger.setLevel(logging.ERROR)

    # 创建一个handler用于控制台输出
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    # 创建第二个handler用于日记记录
    file_handler = logging.FileHandler('D:/Python3.6-32/python0_1/qunar/logs/DB_log.log') if type == 0 else logging.FileHandler('D:/Python3.6-32/python0_1/qunar/logs/data_log.log')
    file_handler.setLevel(logging.ERROR)

    # 自定义handler日记输出格式
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(LOG_FORMAT)
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # 拼接handler
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger