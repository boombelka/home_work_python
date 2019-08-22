# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print('Задание 1')

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
