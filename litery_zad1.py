haslo = str(input('Wpisz hasło: '))
haslo = haslo.lower()

for litera in haslo:
    if litera in 'aeiouy':
            litera=litera.upper()
    print(litera, end=""),

#samo = ('a', 'e', 'i', 'y', 'o', 'u')
#if samo in y:
###
#for x in y:
#    if x in "aeiouy":
#        samo = samo+1
#    else:
#        spol = spol+1
#print(samo,end='')