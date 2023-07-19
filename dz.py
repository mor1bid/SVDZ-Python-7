import os

def work (path, i = 0):
    os.mkdir(path)
    while i <= 3:
        open(path + '/file(' + str(i) + ').txt', 'a')
        i += 1

def renameus(path, myname, ordlen, extold, extmine, border, ordnum = 1):
    path = os.path.abspath(path)
    for z in range(ordlen):
        ordnum *= 10
    for name in os.listdir(path):
        if extold in name:
            file = name.split('.')
            filename = list(file[0])
            myname = list(myname)
            newname = ''
            i = 0
            for l in range(len(filename)):
                if l >= int(border[0]) and l <= int(border[-1]):
                    filename[l] = myname[i]
                    i += 1
                if len(myname) == l:
                    i = 0    
                newname += filename[l]   
                
            print(f'Файл {name} переименован в {newname}_{str(ordnum)}{extmine}')        
            os.rename(path + '/' + name, path + '/' + newname + '(' + str(ordnum) + ')' + extmine)
            ordnum += 1

# 2. Напишите функцию группового переименования файлов. Она должна:
# 1) принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# 2) принимать параметр количество цифр в порядковом номере.
# 3) принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# 4) принимать параметр расширение конечного файла.
# 5) принимать диапазон сохраняемого оригинального имени. 
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

path = input('2. Введите название желаемого каталога\n: ')
if not os.path.exists(path):
    work(path)
myname = input('1) Желаемое конечное имя файлов\n: ')
ordlen = int(input('2) Количество цифр в порядковом номере\n: '))
extold = input('3) Расширение исходных файлов\n: ')
extmine = input('4) Расширение конечных файлов\n: ')
border = input('5) Числовой диапазон сохраняемого оригинального имени (через пробел)\n: ')

renameus(path, myname, ordlen, extold, extmine, border)
