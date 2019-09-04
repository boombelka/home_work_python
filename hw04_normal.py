# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
import re
import random as r
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

print('Задача 1')
# решение с re
pattern = r'[a-z]+'
temp = re.findall(pattern, line)
print(temp)
# решение без re
def parser_not_re(allstring):
       temp = []
       simbol_not_upper = ''
       for i  in range(len(allstring)):
              if  allstring[i].isupper():
                     if not simbol_not_upper == '':
                            temp.append(simbol_not_upper)
                            simbol_not_upper = ''
                     else:
                            pass

              else:
                     simbol_not_upper = simbol_not_upper + allstring[i]

       temp.append(simbol_not_upper) #последний символ не попадает под цикл
       return(temp)

print(parser_not_re(line))
print(re.findall(pattern, ('mtMmEZUOmcq')))
print(parser_not_re('mtMmEZUOmcq'))



# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
#line_2 = 'ddsMMMMMMddddMMMMMss'

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

print('Задача 2')
# c re
pattern2 = r'([a-z]{2})([A-Z]+)([A-Z]{2})'
temp2 = re.findall(pattern2, line_2)
centr_part_temp2 = [p[1] for p in temp2]
print(f'полученная строка с re: {centr_part_temp2}')


# без re
def upper_simbol(line):
       temp2 = []
       lower = ''
       simbol_not_upper = ''
       for i in range(0 , len(line)-5):
              n = i+2
              lower = line[i : n]
              if lower.islower():
                     index_upper = i + 2
                     simbol_not_upper = ''
                     while line[index_upper].isupper():
                            simbol_not_upper = simbol_not_upper + line[index_upper]
                            index_upper = index_upper + 1
                     if len(simbol_not_upper) >= 3:
                            x = len(simbol_not_upper)
                            temp2.append(simbol_not_upper[0:x-2])
                     else:
                            continue
              else:
                     pass
       return(temp2)



print(f'полученная строка без re:{upper_simbol(line_2)}')



# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
print('Задание 3')

MAX_NUMBER = 2500


def arr_number(spisok):

       # Запись в файл
       path = 'data\\' + 'text' + '.txt'
       with open(path, 'w', encoding='UTF-8') as file:
              file.write(str(spisok))
              print(path)

       # Чтение файла
       list = []
       with open(path, 'r', encoding='UTF-8') as file:
              stroka_1 = file.read()
              temp = stroka_1[0]
        # создание списка с группированными числами
       for i in range(1, 2499):
              if stroka_1[i-1] == stroka_1[i]:
                     temp = temp + stroka_1[i]

              else:
                     list.append(temp)
                     temp = stroka_1[i]
       return(list) # возвращает список считанный из файла и сгруппированный по группам чисел


def arr_group_number(list_gr, lenth):
# функция получает сгруппированный список, выясняет длинну самой большой последовательности
    for i in range(0, len(list_gr)):
        if lenth < len(list_gr[i]):
             lenth = len(list_gr[i])
        else:
             continue
    list_max_group_number = []
# на основе самой большоей длинны - находит последовательность чисел
    for i in range(0, len(list_gr)):
        count = len(list_gr[i])
        if lenth == count:
            list_max_group_number.append(list_gr[i])
        else:
            continue
    return(list_max_group_number)



spisok = [r.randint(0, 9) for _ in range(MAX_NUMBER)]
spisok = ''.join(list(map(lambda x: str(x), spisok)))
group_namber = arr_number(spisok)
max_lenth = 0
arr = arr_group_number(group_namber, max_lenth)
print(f'самые большие последовательности чисел в списке: {arr}')
