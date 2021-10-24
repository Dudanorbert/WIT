kapital_po=int(input('Podaj swój kapitał początkowy: '))
miesieczne_wp=int(input('Podaj swoje miesieczne wplywy: '))
miesiace=int(input('ile potrzebujesz miesięcy na inswestycje: '))
koniec=int(input('Podaj pożądaną kwotę: '))
x = kapital_po
y =(miesieczne_wp*miesiace)/100
z = 98*y

#print ('Kwota którą uzbierasz to',(int(x+z)))
if int(x+z)>koniec:
    print('Kwota którą uzbierasz to',(int(x+z)), 'zł, dobrze, jest większa niż planowana końcowa wartość')
elif int(x+z) < koniec:
    print('Kwota którą uzbierasz to',(int(x+z)), 'zł, niestety jest mniejsza niż planowana końcowa wartość')


