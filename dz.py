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
                # if len(myname) != l:
                    filename[l] = myname[i]
                    i += 1
                if len(myname) == l:
                    i = 0    
                newname += filename[l]   
                
            print(f'Файл {name} переименован в {newname}_{str(ordnum)}{extmine}')        
            os.rename(path + '/' + name, path + '/' + newname + '(' + str(ordnum) + ')' + extmine)
            ordnum += 1
            
path = input('2. Введите название желаемого каталога\n: ')
if not os.path.exists(path):
    work(path)
myname = input('1) Желаемое конечное имя файлов\n: ')
ordlen = int(input('2) Количество цифр в порядковом номере\n: '))
extold = input('3) Расширение исходных файлов\n: ')
extmine = input('4) Расширение конечных файлов\n: ')
border = input('5) Числовой диапазон сохраняемого оригинального имени (через пробел)\n: ')

#debug
# path = 'hive'
# myname = 'bee'
# ordlen = 3
# extold = '.png'
# extmine = '.txt'
# border = [0, 3]

renameus(path, myname, ordlen, extold, extmine, border)