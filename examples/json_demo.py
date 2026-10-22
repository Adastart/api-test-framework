"""
JSON 序列化与反序列化示例
字典 <-> JSON 字符串，文件读写
"""
import json

# ============ 1. 字典转 JSON 字符串（序列化） ============
data = {'name': '张三', 'password': '123456', 'male': True, 'money': None}
str_data = json.dumps(data)
print(str_data)
# 输出: {"name": "\u5f20\u4e09", "password": "123456", "male": true, "money": null}

# 格式化输出
print(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False))


# ============ 2. JSON 字符串转字典（反序列化） ============
res_text = '{"name": "张三", "password": "123456", "male": true, "money": null}'
res_dict = json.loads(res_text)
print(res_dict['name'])  # 张三


# ============ 3. 字典写入 JSON 文件 ============
data_dict = {'name': '张三', 'password': '123456', 'male': True, 'money': None}
with open('demo1.json', 'w', encoding='utf-8') as f:
    json.dump(data_dict, f)


# ============ 4. 从 JSON 文件读取 ============
with open('demo2.json', 'r', encoding='utf-8') as f:
    f_dict = json.load(f)
    print(f_dict['name'])
