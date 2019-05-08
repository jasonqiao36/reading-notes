"""
列表推导用于加工“序列”类型
可读性好
Python2.x中有变量泄露问题
"""

symbols = '$¢£¥€¤'

codes = [ord(symbol) for symbol in symbols]

print(codes)