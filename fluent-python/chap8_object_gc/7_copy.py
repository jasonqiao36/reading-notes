l1 = [3, [66, 55, 44], (7, 8, 9)]

l2 = list(l1)  # 浅复制

l1.append(100)

l1[1].remove(55)

print(f'l1: {l1}')
print(f'l2: {l2}')

l2[1] += [33, 22]
l2[2] += (10, 11)

print(f'l1: {l1}')
print(f'l2: {l2}')
