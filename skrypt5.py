logowanie = False
while not logowanie:
    username = input('Podaj login: ')
    password =input('Podaj haslo: ')
    if username =='Admin' and password == '1234':
        logowanie = True
print('Zalogowano pomyślnie:)')


