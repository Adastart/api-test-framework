"""
主运行入口
执行全部测试用例，生成 HTML 报告并发送邮件
"""
import unittest
import os
import sys

sys.path.append('..')
from config.config import *
from lib.send_email import send_email

# HTMLTestRunner 放在 lib 目录下
from lib.HTMLTestRunnerCN import HTMLTestRunner


if __name__ == '__main__':
    logging.info("=" * 50 + "测试开始" + "=" * 50)

    # 从配置文件读取用例路径
    suite = unittest.defaultTestLoader.discover(test_path)

    # 生成 HTML 测试报告
    with open(report_file, 'wb') as f:
        HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="卡卡").run(suite)

    # 发送邮件
    send_email(report_file)

    logging.info("=" * 50 + "测试结束" + "=" * 50)
