lista1_1 = []
for x in range(3,14):
    lista1_1.append(x)

print("lista1_1 =",lista1_1)

print('\n')

lista1_2 = [i for i in range(3,14)]
print("lista1_2 =",lista1_2)

print('\n')

x=-1
lista2=[]
while x!=10:
        x+=1
        lista2.append(x)
        if len(lista2)==11:
            print("lista2 =",lista2)
