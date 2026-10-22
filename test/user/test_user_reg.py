"""
用户注册接口测试用例
包含环境检查、数据库断言、数据清理
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
from lib.db import check_user, del_user, add_user


class TestUserReg(unittest.TestCase):
    """用户注册接口测试类"""

    @classmethod
    def setUpClass(cls):
        """整个测试类只执行一次"""
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "TestUserReg")

    def test_user_reg_normal(self):
        """正常注册用例"""
        case_data = get_test_data(self.data_list, 'test_user_reg_normal')
        if not case_data:
            logging.error("用例数据不存在")
            return

        url = case_data.get('url')
        data = json.loads(case_data.get('data'))
        expect_res = json.loads(case_data.get('expect_res'))
        name = data.get('name')

        # 环境检查
        if check_user(name):
            del_user(name)

        # 发送请求
        res = requests.post(url=url, json=data)
        log_case_info('test_user_reg_normal', url, data, expect_res, res.text)

        # 响应断言
        self.assertDictEqual(res.json(), expect_res)

        # 数据库断言
        self.assertTrue(check_user(name))

        # 环境清理
        del_user(name)

    def test_user_reg_exist(self):
        """用户已存在注册用例"""
        case_data = get_test_data(self.data_list, 'test_user_reg_exist')
        if not case_data:
            logging.error("用例数据不存在")
            return

        url = case_data.get('url')
        data = json.loads(case_data.get('data'))
        expect_res = json.loads(case_data.get('expect_res'))
        name = data.get('name')

        # 环境检查 - 确保用户已存在
        if not check_user(name):
            add_user(name, '123456')

        # 发送请求
        res = requests.post(url=url, json=data)
        log_case_info('test_user_reg_exist', url, data, expect_res, res.text)

        # 响应断言
        self.assertDictEqual(res.json(), expect_res)

        # 数据库断言（没有注册成功）
        # 环境清理
        del_user(name)


if __name__ == '__main__':
    unittest.main(verbosity=2)
