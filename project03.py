# coding=utf-8
# Эта программа переводит числа из десятичной системы счисления в другую, вплоть до 25-ой.
# 8889645 в 25

number = int(input('Введите чило в десятичной системе счисления: '))
number_system = int(input('Введите систему счисления '))
a = number
s = []
sit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']


while a > 1:
    d = a % number_system
    for i in range(len(sit)):
        if d == i + 1:
            d = sit[i]
    s.append(d)
    a = a // number_system
if a > 0:
    s.append(a)
s.reverse()
st = ''
for i in s:
    st += str(i)
print('Число в', number_system, '-ной системе:', st)
