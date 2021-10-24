wiek=int(input('Cześć, ile masz lat?'))
if wiek > 21:
    print('Możesz prowadzić samochód oraz głosować w wyborach.')
elif wiek > 17 and wiek < 21:
    print('Możesz prowadzić samochód')
elif wiek < 17:
    print('Nie możesz prowadzić samochodu oraz głosować w wyborach')

