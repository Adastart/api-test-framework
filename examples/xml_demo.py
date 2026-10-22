"""
XML 解析示例
使用 ElementTree 解析 XML 数据
"""
from xml.etree import ElementTree as ET

# XML 数据
d = '''<bookstore>
  <book category="COOKING">
    <title lang="en">Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>
  <book category="CHILDREN">
    <title lang="en">Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
  <book category="WEB">
    <title lang="en">Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>39.95</price>
  </book>
</bookstore>'''

# 加载元素树
root = ET.fromstring(d)

print(root.tag)  # 当前节点 bookstore

# 查找所有 book 子节点
print(root.findall('book'))

# 查找第三个 book
print(root.find('book[2]'))

# 查找 category 属性为 COOKING 的 book
print(root.find("book[@category='COOKING']"))

# 查找 category 为 WEB 的 book 下的 title 文本
print(root.find("book[@category='WEB']/title").text)
