# Гостевая книга: напишите цикл while, который в цикле запрашивает у пользователей имена. 
# При вводе каждого имени выведите на экран приветствие и добавьте строку с сообщением в файл с именем guest_book.txt. 
# Проследите за тем, чтобы каждое сообщение размещалось в отдельной строке файла.

with open('file3.txt', 'a') as fils:
    f=0
    while f!=3:
        name=input('enter your name:')
        fils.write('\n'+'Hello, '+str(name))
        f+=1

    
