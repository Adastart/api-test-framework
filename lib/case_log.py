"""
测试用例日志封装
统一输出请求参数、响应结果等日志信息
"""
from config.config import *
import json


def log_case_info(case_name, url, data, expect_res, res_text):
    """
    输出测试用例执行日志
    :param case_name: 用例名称
    :param url: 请求地址
    :param data: 请求数据
    :param expect_res: 预期结果
    :param res_text: 实际响应结果
    """
    if isinstance(data, dict):
        data = json.dumps(data, ensure_ascii=False)

    logging.info("测试用例：{}".format(case_name))
    logging.info("url：{}".format(url))
    logging.info("请求参数：{}".format(data))
    logging.info("期望结果：{}".format(expect_res))
    logging.info("实际结果：{}".format(res_text))
