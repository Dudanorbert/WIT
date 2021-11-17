#import intersection

lista1=[1,2,3,4,5]
lista11=set(lista1)
lista2=[1,2,3,4,5]
lista22=set(lista2)
lista3=[1,2,2,3,3,4,5]
lista33=set(lista3)
odpowiedz=[]
#b=set(lista1)&set(lista2)&set(lista3)
#print(b)
#set1=lista1.intersection(lista2)
#resoult_set=set1.intersection(lista3)
#final_list=list(resoult_set)
#print(final_list)

res = []
for i in lista1:
    if i not in res:
        res.append(i)
x=len(lista1)-len(res)
if len(lista1)-len(res)!=0:
    odpowiedz.append("lista1 zawiera duplikaty")
    #print("lista1 zawiera duplikaty")

res2 = []
for i in lista2:
    if i not in res2:
        res2.append(i)
y=len(lista2)-len(res2)
if len(lista2)-len(res2)!=0:
    odpowiedz.append("lista2 zawiera duplikaty")
    #print("lista2 zawiera duplikaty")

res3 = []
for i in lista3:
    if i not in res3:
        res3.append(i)
z=len(lista3)-len(res3)
if len(lista3)-len(res3)!=0:
    odpowiedz.append("lista 3 zawiera duplikaty")
   #print("lista 3 zawiera duplikaty")

if(lista11==lista22==lista33):
    print ("Wszystkie listy zawierają te same elementy",*odpowiedz, sep=", ")
   