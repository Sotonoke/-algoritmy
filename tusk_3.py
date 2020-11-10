# Определить, какое число в массиве встречается чаще всего.

from random import random

n = 10
arr = [0] * n
for i in range(n):
    arr[i] = int(random() * 20)
print(arr)

num = arr[0]
m_frq = 1
for i in range(n - 1):
    frq = 1
    for k in range(i + 1, n):
        if arr[i] == arr[k]:
            frq += 1
    if frq > m_frq:
        m_frq = frq
        num = arr[i]

if m_frq > 1:
    print(m_frq, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')