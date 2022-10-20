exercitiu = input('Ce exercitiu vrei sa ruleze? Variante: 1, 2-3, S1 sau S2?\n')

# #1. Parola unui sistem este: Passme1n. Cereți input de la utilizator cu parola. Afișați pe
# ecran un mesaj (True, False) daca aceasta este Passme1n, respectiv dacă nu este
# aceasta.

# /////REZOLVARE EXERCITIU 1/////
match exercitiu:
    case '1':

        password = 'Passme1n'
        user_input = input('Introdu parola:')

        if password == user_input:
            print('Parola corecta!')
        else:
            print('Parola incorecta!')

    # 2. Cereți ca input de la utilizator 2 nume. Verificati si afisati:
    # - Lungimea primului nume
    # - Dacă cele doua nume date sunt la fel
    # - Dacă primul nume este mai lung decat al doilea nume
    # - Inițiala primului nume
    # - Primul nume inversat

    # /////REZOLVARE EXERCITIU 2/////
    case '2-3':

        nume1 = input('Introduceti primul nume:')
        nume2 = input('Introduceti al doilea nume:')

        print('Primul nume introdus:', nume1, '\nAl doilea nume introdus:', nume2)

        print('Primul nume are', len(str(nume1)), 'caractere!')
        if (len(str(nume1))) == (len(str(nume2))):
            print('Cele 2 nume sunt la fel!')
        else:
            print('Cele 2 nume sunt diferite!')

        if len(str(nume1)) == len(str(nume2)):
            print('Cele 2 nume au acelasi numar de caractere!')
        else:
            print('Cele 2 nume nu au acelasi numar de caractere!')

        print('Initiala primului nume este:', nume1[1])
        print(nume1[::-1])

        # /////EXERCITIU 3/////
        # 3. Folosind codul de la exercitiul 2, mai cereți input de la utilizator cu un număr:
        # - Afisati primul nume multiplicat de n ori, unde n este numărul introdus de către
        # utilizator.

        numar = input('Introduceti un numar:')
        numar = int(numar)
        print(numar * nume1)

    # #4. Declarați o variabila cu șirul: “Ananas”. Afișati șirul în următoarele feluri pe ecran:
    # - A
    # n
    # a
    # n
    # a
    # s
    # - Ana
    # nas
    # - An:ana:s
    # - Ana_na_s
    # - nananananananana

    # /////REZOLVARE EXERCITIU 4/////
    case 'S1':

        my_var = 'Ananas'

        print(my_var[0])
        print(my_var[1])
        print(my_var[2])
        print(my_var[3])
        print(my_var[4])
        print(my_var[5])
        print(my_var[0:3])
        print(my_var[3:6])
        print(my_var[0:1], my_var[1:3], my_var[3:5], sep=':')
        print(my_var[1:3] * 8)

    # /////SUPLIMENTAR 1//////
    case 'S2':

        nume = input('Introduceti un cuvant:')
        nume = nume.lower()
        if nume == nume[::-1]:
            print('Cuvantul este un palindrom')
        else:
            print('Cuvantul nu este un palindrom')

        # /////SUPLIMENTAR 2//////
        nume = input('Introduceti un sir:')
        NUME = nume.upper()
        print(NUME, nume)

        if nume[0] == NUME[0]:
            print('Sirul incepe cu o majuscula: True')
        else:
            print('Sirul incepe cu o majuscula: False')

    case _:
        print("pe asta nu l-am facut :(  Alege una din variantele de mai sus.")
