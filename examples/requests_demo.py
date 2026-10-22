"""
requests 库基础用法示例
包含 GET/POST 请求、参数传递、响应解析等
"""
import requests
import json

# ============ 1. 最简单的 GET 请求 ============
# 组装请求 -> 发送请求 -> 解析响应
url = "http://httpbin.org/get"
res = requests.get(url=url)  # res 是响应对象
print(res.text)  # 输出响应文本


# ============ 2. 带参数的 GET 请求 ============
# 方式一：参数直接写在 URL 里
url1 = "http://www.tuling123.com/openapi/api?key=ec961279f4534590b9248f0aeb6600bbe&info=你好"
res1 = requests.get(url=url1)
print(res1.text)

# 方式二：params 参数传递（推荐）
url2 = "http://www.tuling123.com/openapi/api"
params = {"key": "ec961279f4534590b9248f0aeb6600bbe", "info": "你好"}
res2 = requests.get(url=url2, params=params)
print(res2.text)


# ============ 3. 传统表单类 POST 请求 (x-www-form-urlencoded) ============
url3 = "http://httpbin.org/post"
data = {"name": "hanzhichao", "age": 18}
res3 = requests.post(url=url3, data=data)
print(res3.text)


# ============ 4. JSON 类型 POST 请求 (application/json) ============
url4 = "http://openapi.tuling123.com/openapi/api/v2"
data = {
    "reqType": 0,
    "perception": {
        "inputText": {"text": "附近的酒店"}
    },
    "userInfo": {
        "apiKey": "ec961279f4534590b9248f0aeb6600bbe",
        "userId": "206379"
    }
}
# 方式一：json 参数直接传字典
res4 = requests.post(url=url4, json=data)
print(res4.text)

# 方式二：手动设置 headers 和 json.dumps
headers = {"Content-Type": "application/json"}
res4b = requests.post(url=url4, data=json.dumps(data), headers=headers)
print(res4b.text)


# ============ 5. 响应对象解析 ============
res = requests.get("https://www.baidu.com")
print(res.status_code)  # HTTP 状态码
print(res.reason)  # 状态码含义
print(res.text)  # 响应文本（有乱码）
print(res.content)  # 二进制内容
print(res.encoding)  # 当前编码 ISO-8859-1
print(res.apparent_encoding)  # 真实编码 utf-8
res.encoding = 'utf-8'  # 手动设置编码
print(res.text)
print(res.cookies)  # CookieJar 对象
print(res.cookies.get('BDORZ'))  # 获取指定 cookie


# ============ 6. Session 会话保持 ============
s = requests.session()  # 新建会话
s.post(url="https://demo.fastadmin.net/admin/index/login.html",
       data={"username": "admin", "password": "123456"})
res = s.get("https://demo.fastadmin.net/admin/dashboard?ref=addtabs")
print(res.text)


# ============ 7. Basic Auth 授权 ============
res = requests.get("https://api.github.com/user",
                  auth=("hanzhichao", "hanzhichao123"))
print(json.dumps(res.json(), indent=2, ensure_ascii=False))
