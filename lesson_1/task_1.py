# https://drive.google.com/file/d/1jxT8cqAY5BRUcxyvBRZJencOrt1SVbS8/view?usp=sharing
# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
n = int(input('Введите трехзначное число: '))

a = n // 100
b = n % 100 // 10
c = n % 10
summa = a + b + c
mnz = a * b * c

print('Сумма цифр числа = ', summa)
print('Произведение цифр числа =   ', mnz)

