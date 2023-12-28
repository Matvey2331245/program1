p=0
b=''
ar=[]
count=0
f=open("text.txt", 'r')
text=f.read()
print(text)
p=len(text)
print(p)
if p!=0:
    for l in text:
        if l.isupper() and l!=' ':
            if l not in ar:
               b=l
               print(b)
               ar=ar+[l]
               for b in text:
                   if b == l:
                    count=count+1

            print('=',count)
            count=0
#print('Количество строчных букв =',count)
f.close()

