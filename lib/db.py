"""
数据库操作封装
支持查询、修改、事务回滚等常用操作
"""
import pymysql
import sys
sys.path.append('..')
from config.config import *


def get_db_conn():
    """获取数据库连接"""
    conn = pymysql.connect(host=db_host,
                           port=db_port,
                           user=db_user,
                           passwd=db_passwd,
                           db=db,
                           charset='utf8')
    return conn


def query_db(sql):
    """封装查询数据库操作"""
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result


def change_db(sql):
    """封装更改数据库操作（带事务回滚）"""
    conn = get_db_conn()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        logging.error(str(e))
    finally:
        cur.close()
        conn.close()


def check_user(name):
    """检查用户是否存在"""
    result = query_db("select * from user where name = '{}'".format(name))
    return True if result else False


def add_user(name, password):
    """添加用户"""
    sql = "insert into user (name, passwd) values ('{}','{}')".format(name, password)
    change_db(sql)


def del_user(name):
    """删除用户"""
    sql = "delete from user where name='{}'".format(name)
    change_db(sql)
