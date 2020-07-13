# В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную. 
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу. 

f=open('f1.txt')
while True:
    line=f.readlines(2)
    if not line:
        break
    print(line)
f.close()






# with open('class1.txt', 'r') as file5:
#     summa=0
#     x=0  
#     m=0  
#     for i in file5:
#         m=int(i[len(i)-2])
#         summa+=m
#         x+=1
#         if m<3:
#             print(i)
    # print("average mark:",round(summa/x,2))