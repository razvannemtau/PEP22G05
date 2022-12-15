# def num_there(string):
#     for letter in string:
#         for i in range(10):
#             if letter == str(i):
#                 return True
# def login():
#     a = input('Introducti o parola')
#     while True:
#         ask_again = False
#         if (len(a)) < 7:
#             print ('Parola prea scurta')
#             ask_again=True
#         if num_there(a) != True:
#             print ('parola nu are cifra')
#             ask_again=True
#         if ask_again == False:
#             break
#         else:
#             a = input('Introducti o parola')
#
# result=login()
# print(result)

#################################################################################
#
# def num_there(string: str):
#     for letter in string:
#         if letter.isnumeric():
#             return True
# def num_special(string: str):
#     for letter in string:
#         if not letter.isalnum():
#             return True
# def login():
#     a = input('Introducti o parola')
#     while True:
#         ask_again = False
#         if (len(a)) < 7:
#             print('Parola prea scurta')
#             ask_again = True
#         if num_there(a) != True:
#             print('parola nu are cifra')
#             ask_again = True
#         if num_special(a) != True:
#             print('parola nu are caractere speciale')
#             ask_again = True
#         if a != a.capitalize():
#             print('prima litera nu este mare')
#             ask_again = True
#         if ask_again == False:
#             break
#         else:
#             a = input('Introducti o parola')
#
#
# result = login()
# print(result)

############################################################################
def aaa (a,b):
    return int(a)**int(b)



def ridicare_la_putere ():
    while True:
        data = input("please provide numbers:")
        if data == 'q':
            break
        a, b = data.split(",")
        print('result is', aaa(a,b))

ridicare_la_putere()


