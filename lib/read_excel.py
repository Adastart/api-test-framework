"""
Excel 数据读取封装
从 Excel 文件中读取测试数据，返回字典列表
"""
import xlrd


def excel_to_list(data_file, sheet):
    """
    读取 Excel 文件，返回字典列表
    :param data_file: Excel 文件路径
    :param sheet: 工作表名称
    :return: 字典列表，每个元素是一行数据
    """
    data_list = []
    wb = xlrd.open_workbook(data_file)
    sh = wb.sheet_by_name(sheet)
    header = sh.row_values(0)  # 获取标题行数据
    for i in range(1, sh.nrows):  # 跳过表头，从第二行开始读取数据
        d = dict(zip(header, sh.row_values(i)))
        data_list.append(d)
    return data_list


def get_test_data(data_list, case_name):
    """
    从数据列表中查找指定用例的数据
    :param data_list: 全部数据列表
    :param case_name: 用例名称
    :return: 匹配到的用例数据，找不到返回 None
    """
    for case_data in data_list:
        if case_name == case_data['case_name']:
            return case_data
    return None


if __name__ == '__main__':
    # 测试读取 Excel 数据
    data_list = excel_to_list("../data/test_user_data.xlsx", "TestUserLogin")
    case_data = get_test_data(data_list, 'test_user_login_normal')
    print(case_data)
