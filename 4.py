dane_logowania={'login':'ND','haslo':'JP'}
uzytkownik= False
while not uzytkownik:
    Login=input("Podaj nazwę użytkownika: ")
    Haslo=input("Podaj haslo użytkownika: ")
    if Login == dane_logowania['login'] and Haslo == dane_logowania['haslo']:
        logowanie = True
        print('Logowanie poprawne')
        break
    elif Login != dane_logowania['login'] or Haslo != dane_logowania['haslo']:
        print('Błąd! Wprowadź dane ponownie.')
        

    


