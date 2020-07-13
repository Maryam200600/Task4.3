f=open('f4.txt','r')
while True:
    line=f.readlines(5)
    if not line:
        break
    print(line)
f.close()