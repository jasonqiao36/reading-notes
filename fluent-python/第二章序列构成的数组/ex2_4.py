colors = ['黑', '白']
sizes = ['S', 'M', 'L']

tshirts1 = [(color, size) for color in colors for size in sizes]  # 先按颜色排序
print(tshirts1)

tshirts2 = [(color, size) for size in sizes for color in colors]  # 先按大小排序
print(tshirts2)
