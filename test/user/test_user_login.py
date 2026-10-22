"""
用户登录接口测试用例
数据驱动：从 Excel 读取测试数据
"""
import unittest
import requests
import json
import os
import sys

sys.path.append('../..')
from config.config import *
from lib.read_excel import *
from lib.case_log import log_case_info


class TestUserLogin(unittest.TestCase):
    """用户登录接口测试类"""

    @classmethod
    def setUpClass(cls):
        """整个测试类只执行一次"""
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "TestUserLogin")

    def test_user_login_normal(self):
        """正常登录用例"""
        case_data = get_test_data(self.data_list, 'test_user_login_normal')
        if not case_data:
            logging.error("用例数据不存在")
            return

        url = case_data.get('url')
        data = json.loads(case_data.get('data'))
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url, data=data)
        log_case_info('test_user_login_normal', url, data, expect_res, res.text)
        self.assertIn(expect_res, res.text)

    def test_user_login_password_wrong(self):
        """密码错误登录用例"""
        case_data = get_test_data(self.data_list, 'test_user_login_password_wrong')
        if not case_data:
            logging.error("用例数据不存在")
            return

        url = case_data.get('url')
        data = json.loads(case_data.get('data'))
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url, data=data)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertIn(expect_res, res.text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
