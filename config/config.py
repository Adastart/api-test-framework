"""
全局配置文件
日志、数据库、邮件等配置统一在此维护
"""
import logging
import os

# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级目录
data_path = os.path.join(prj_path, 'data')  # 数据目录
test_path = os.path.join(prj_path, 'test')  # 用例目录

# 日志文件路径
log_file = os.path.join(prj_path, 'log', 'log.txt')  # 日志文件
report_file = os.path.join(prj_path, 'report', 'report.html')  # 测试报告

# 日志配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式

# 数据库配置
db_host = '127.0.0.1'
db_port = 3306
db_user = 'root'
db_passwd = '123456'
db = 'api_test'

# 邮件配置
smtp_server = 'smtp.sina.com'
smtp_user = '15701374212@163.com'
smtp_password = ''

sender = smtp_user  # 发件人
receiver = '1064420684@qq.com'  # 收件人
subject = '接口测试报告'  # 邮件主题
