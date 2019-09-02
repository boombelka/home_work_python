# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil

#Функция создающая директорию
def creat_dir(name):
    os.mkdir(name)

#  удаляет папки
def del_dir(name):
    os.rmdir(name)

# показывает папки в директории
def list_dir_(path="."):
    os.listdir(path)
    lsdir = []
    list = os.listdir(path)
    for i in range(0, len(list)):
        if os.path.isdir(list[i]) == True:
            lsdir.append(list[i])
        else:
            pass
    return(lsdir)


def copy_file(sourse, target):
    try:
        shutil.copy(sourse, target)
    except FileExistsError:
        print('Такой файл уже существует')




def remove_file(filename):
    os.remove(filename)



"""
НИЖЕ ЗАКОМЕНТИРОВАННО, Чтобы работала связка с файлом normal
#список папок
list_dir = ["dir_1", "dir_2", "dir_3", "dir_4", "dir_5", "dir_6", "dir_7", "dir_8", "dir_9"]
#скрипт создающий папки
input('нажмите любую клавишу сейчас создадим 9 папок')
for i in range(0, len(list_dir)):
    creat_dir(list_dir[i])
# скрипт удаляющий папки
print(f'папки {list_dir} созданы')
input('нажмите любую клавишу сейчас удалим 9 папок')
for i in range(0, len(list_dir)):
    del_dir(list_dir[i])
input(f'папки {list_dir} удалены')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print(f'{list_dir_(path=".")}')

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
sourse = 'hw05_easy.py'
target = 'hw05_easy_copy.py'
shutil.copy(sourse, target)
input('нажмите любую клавишу')
os.remove("hw05_easy_copy.py")

"""