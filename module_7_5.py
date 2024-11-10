# ЗАДАНИЕ ПО ТЕМЕ "Файлы в операционной системе"

import os
import time

os.chdir('+5МодульТильда 7')
directory = os.getcwd()
print('Текущая директория: ', directory)

for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(directory, file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
