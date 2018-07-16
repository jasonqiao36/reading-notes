symbols = '$¢£¥€¤'

ord_symbol = tuple(ord(symbol) for symbol in symbols)
print(ord_symbol)

import array

array.array('I', (ord(symbol) for symbol in symbols))
