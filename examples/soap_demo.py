"""
SOAP/WebService 接口调用示例
两种方式：suds 客户端 和 requests 库
"""
# ============ 方式一：使用 suds 客户端 ============
# 安装: pip install suds-jurko
from suds.client import Client

service = Client("http://115.28.108.130:4000/?wsdl").service
result = service.addUser("范冰冰", "123456")
print(result)  # 输出: 用户已存在


# ============ 方式二：使用 requests 发送 SOAP 请求 ============
import requests

url = 'http://115.28.108.130:4000/'
data = '''<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:user="UserService">
   <soapenv:Header/>
   <soapenv:Body>
      <user:addUser>
         <!--Optional:-->
         <user:name>张三</user:name>
         <!--Optional:-->
         <user:password>123456</user:password>
      </user:addUser>
   </soapenv:Body>
</soapenv:Envelope>'''.encode('utf-8')

res = requests.post(url=url, data=data)
print(res.text)
