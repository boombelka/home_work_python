# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
"""

def fraction(operation):

    list = []
    finger1 = []
    finger2 = []
    list = operation.split(' ')
    print(list)
    finger1 = list[0].split('/')
    print(finger1)
    finger2 = list[2].split('/')
    print(finger2)
    if finger1[1] == '/' and finger2[1] == '/':
        down_part = int(finger1[2]) * int(finger2[2])
        if list[1] == '+':
            up_part = int(finger1[0]) * down_part + int(finger2[0]) * down_part
        else:
            up_part = int(finger1[0]) * down_part + int(finger2[0]) * down_part
    elif finger1[1] == '/' and len(finger) == 1:
        down_part = int(finger1[2])
        if list[1] == '+':
            up_part = int(finger1[0]) * down_part + int(finger2[0]) * down_part
        else:
            up_part = int(finger1[0]) * down_part - int(finger2[0]) * down_part
    elif len(finger1) == 1 and finger2[1] == '/':
        down_part = int(finger2[2])
        if list[1] == '+':
            up_part = int(finger1[0]) * down_part + int(finger2[0]) * down_part
        else:
            up_part = int(finger1[0]) * down_part + int(finger2[0]) * down_part
    else:
        pass
#    full = up_part // down_part
#    up_part_end = up_part - down_part * full
#    print(f'{full}  {up_part_end}/{down_part}')


print('Задание 1')
operation = input(f'Введите выражение:')
fraction(operation)
"""
# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
def work_file():

    list = []
    basa = {}
    with open('E:\python\home_work_python\data\workers.txt', 'r', encoding='UTF-8') as file:
        #for i in range(0,4):
        list = file.readlines()
        #for line in file:
        for i in range(0, 3):
            m = list[i]
            list[i] = m.split("|")
        print(list)
        norma = (str(list[0][1]))
        for i in range(1, 3):
            u = 0
            figer = False
            while figer == False:
                n = 0
                if list[i][u].isdigit() == True:
                    n = n + list[i][u]
                else:
                    hour = n - norma
                    if hour > 0:
                        zp = hour/norma
                        base[list[i][0]] = str(zp)
                        break
        print(base)


def process():
    pass


work_file()

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
