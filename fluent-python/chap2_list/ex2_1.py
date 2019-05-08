symbols = '$¢£¥€¤'

codes = []

for symbol in symbols:
    codes.append(ord(symbol))   # ord获取unicode码位(codepoint)

print(codes)
