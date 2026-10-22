"""
Flask 搭建 Mock 接口示例
模拟用户注册接口，随机返回不同响应
"""
from flask import Flask, request, jsonify, abort
import random

app = Flask(__name__)


@app.route("/api/user/reg/", methods=["POST"])
def reg():
    # 校验必填参数
    if not request.json or not 'name' in request.json or not 'password' in request.json:
        abort(400)

    res = [
        # 成功响应
        {"code": "100000", "msg": "成功", "data": {"name": "李四", "password": "e10adc3949ba59abbe56e057f20f883e"}},
        # 用户已存在
        {"code": "100001", "msg": "失败，用户已存在", "data": {"name": "李四", "password": "e10adc3949ba59abbe56e057f20f883e"}},
        # 失败响应
        {"code": "100002", "msg": "失败，添加用户失败", "data": {"name": "李四", "password": "e10adc3949ba59abbe56e057f20f883e"}},
    ]

    return jsonify(random.choice(res))


if __name__ == '__main__':
    app.run()
