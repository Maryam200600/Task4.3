# В текстовом файле посчитать количество строк, а также для каждой
# отдельной строки определить количество в ней символов и слов.
 
with open('file2.txt', 'r') as fils:
    letters=0
    #words=0
    line=0
    s=0
    for i in fils:
        line+=1
        w=1
        words=0
        f=0
        s+=1
        for j in i:
            if j!=' ' and f==0:
                words+=1
                flag=1
            elif j==' ':
                w+=1
                f=0
        print('Количество символов в '+str(s)+' строке='+str(len(i)))
        print('Количество слов='+str(w))
    print('Общее количество строк='+str(line))
   

