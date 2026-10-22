# Python 接口自动化测试框架

基于 Python + requests + unittest 构建的接口自动化测试框架，数据与用例分离，支持 Excel 数据驱动、HTML 测试报告、日志记录和邮件发送。

## 项目结构

```
api_test_framework/
├── config/                 # 配置文件目录
│   └── config.py           # 全局配置（日志、数据库、邮件）
├── lib/                    # 公共方法库
│   ├── db.py               # 数据库操作封装
│   ├── read_excel.py       # Excel 数据读取封装
│   ├── case_log.py         # 测试用例日志封装
│   └── send_email.py       # 测试报告邮件发送
├── data/                   # 测试数据目录
│   └── test_data.xlsx      # Excel 测试数据
├── test/                   # 测试用例目录
│   └── user/               # user 模块用例
│       ├── __init__.py
│       ├── test_user_login.py
│       └── test_user_reg.py
├── log/                    # 日志目录
├── report/                 # 测试报告目录
├── examples/               # 基础示例代码
│   ├── requests_demo.py    # requests 库基础用法
│   ├── json_demo.py        # JSON 序列化与反序列化
│   ├── soap_demo.py        # SOAP/WebService 接口调用
│   ├── xml_demo.py         # XML 解析示例
│   └── mock_server.py      # Flask 搭建 Mock 接口
├── run_all.py              # 主运行入口
└── requirements.txt        # 依赖包列表
```

## 环境依赖

```bash
pip install requests
pip install pymysql
pip install xlrd
```

## 快速开始

1. 修改 `config/config.py` 中的数据库和邮件配置
2. 在 `data/test_data.xlsx` 中维护测试数据
3. 在 `test/user/` 下编写测试用例
4. 运行 `python run_all.py` 执行全部用例并生成报告

## 核心功能

- **数据驱动**：从 Excel 读取测试数据，实现数据与用例分离
- **断言机制**：支持状态码、响应内容、数据库断言
- **测试报告**：生成 HTML 格式测试报告
- **日志记录**：完整记录请求参数、响应结果和执行过程
- **邮件通知**：测试完成后自动发送报告邮件
- **数据库校验**：用例执行前后自动校验数据库状态

## 参考来源

《Python接口测试教程(分节版)》- 韩志超
