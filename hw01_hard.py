﻿#
__author__ = 'Верещагин А.В.'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Подсказка: это значение точно есть ;)


print(' Задание 1')
print(f' inf - бесконечность')
a = float('inf')
print(a == a ** 2)
print (a == a*2)
print (a > 99999)
