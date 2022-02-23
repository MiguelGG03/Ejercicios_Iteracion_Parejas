import math
n=int(input('Numero:\n'))
lista=[]
for i in range (0,n):
    h1=float(math.sqrt(i))
    h2=int(math.sqrt(i))
    if(h1==h2):
        lista.append(i)
print(lista)