# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print('Задание 1')
import math

def fibonacci(n, m):

    list = [1, 1]
    for i in range(2, m):
        i_n = i - 1
        i_m = i - 2
        u = list[i_n] + list[i_m]
        list.append(u)
    print(f'Последовательность фибоначи с N по M элементы: {list[n - 1: m - 1]}')


n = int(input('Введите начало рядо N:'))
m = int(input('Введите конец ряда рядо M:'))
fibonacci(n, m)
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
print('Задание 2')

def sort_to_max(origin_list):
    print(f'Начальный список: {origin_list}')
    for i in range(len(origin_list)-1):
        for u in range(len(origin_list)-i-1):
            if  origin_list[u] > origin_list[u+1]:
                origin_list[u], origin_list[u+1] = origin_list[u+1], origin_list[u]
    print(f'сортированный список по возрастанию:  {origin_list}')
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

print('Задание 3')

def filter_new (arg, list):
    bufer = []
    for i in range(len(list)):
        if arg in list[i]:
            bufer.append(list[i])
        else:
            pass
    print(f'отфильтрованные значения: {bufer}')


list = ['просо', 'пашня', 'пашня', 'мак', 'пашня', 'мак', 'пашня', 'просо', 'пашня', 'максим', ]
arg = input('Введите слово для фильтрации списка')
filter_new(arg, list)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
print('Задание 4')

print('Находим 4 отрезка')
a1 = (1, 2)
a2 = (3, 4)
a3 = (5, 3)
a4 = (3, 1)
x1 = a1[0]
x2 = a2[0]
x3 = a3[0]
x4 = a4[0]
y1 = a1[1]
y2 = a2[1]
y3 = a3[1]
y4 = a4[1]
length1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
length2 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
length3 = math.sqrt((x4 - x3)**2 + (y4 - y3)**2)
length4 = math.sqrt((x1 - x4)**2 + (y1 - y4)**2)
diagonal = math.sqrt((x4 - x2)**2 + (y4 - y2)**2)
print(f'Длина отрезка а1: {length1}')
print(f'Длина отрезка а2: {length2}')
print(f'Длина отрезка а3: {length3}')
print(f'Длина отрезка а4: {length4}')
print(f'Длина диагонали: {diagonal}')
a1a2a4 = diagonal / length3
a3a4a2 = diagonal / length1
if a1a2a4 == a3a4a2 and length1 == length3 and length2 == length4:
    print(f'Фигура - Прямоугольник')
else:
    print(f'Фигура - не прямоугольник')
