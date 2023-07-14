"Приложение Заметки"
from datetime import datetime

collect = {}
d=1
with open('Notes.txt', 'r', encoding='utf-8') as file:       #Прочитать из файла
    for l in file:
        l = l.replace('\n','')
        collect[d] = list(l.split(';'))
        d+=1
dict = collect
path = 'Notes.txt'
print("Здравствуйте ")
while True:    
    # print("Здравствуйте ")
    print("Для того чтобы вывести Заметки, нажмите - 1 ")
    print("Для того чтобы добавить запись, нажмите - 2 ")
    print("Для того чтобы изменить Заметку, нажмите - 3 ")
    print("Для того чтобы удалить Заметку, нажмите - 4 ")
    print("Для завершения, нажмите - 5 ")
    n = input(str())
    t = datetime.now()
    if n == "1":
        print(dict)
        pass
    if n == "2":
        s=1
        save = list(input("Введите Название и текст заметки разделенные ':'\n (Пример: Тема: Текст заметки) : ").split(":"))
        while True:
            if s in dict:
                s+=1
            else:
                save.append(t)
                dict[s] = save
                print("Дата изменения: ")
                print(t)
                break
        print(dict)
        pass
    if n == "3":
        print("Введите Название заметки: ")
        text = input(str())
        for i in dict:                  #поиск по фамилии 
            if dict[i][0] == text:
                print(dict[i])
                print("Вы хотите изменить Название? нажмите 1 ")
                print("Вы хотите изменить текст? нажмите 2 ")
                vib = input(str())
                if vib == "1":
                    print("Введите новое Название: ")
                    vibChange = input(str().split())
                    dict[i][0] = vibChange
                    dict[i][2] = t 
                    print(dict[i])
                if vib == "2":
                    print("Введите техт: ")
                    fioChange = input(str().split())
                    dict[i][1] = fioChange
                    dict[i][2] = t 
                    print(dict[i])
            else:
                print("Заметка не найдена")
        pass
    if n == "4":
        print("Введите Название заметки: ")
        title = input(str())
        for i in dict:                  #поиск по фамилии 
            if dict[i][0] == title:
                print(dict[i])
                print("Вы точно хотите удалить заметку? нажмите 1")
                print("Если вы передумали удалять заметку, нажмите 2")
                q = input(str())
                if q == "1":
                    del dict[i]
                    print("Заметка удалена")
                    print(dict)
                    break
                if q == "2":
                    pass
    if n == "5":
        print("Спасибо за пользование программой. До свидания!")
        break

with open('Notes.txt', 'w', encoding='utf-8') as file:    # запись в файл
    for k in dict:
        file.write(f'{dict[k][0]};{dict[k][1]};{dict[k][2]}\n')
        