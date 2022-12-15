# parola=7788
# b=range(3)
# for i in b:
#     a = int(input('Introduceti o parola: '))
#     if(a==parola):
#         print('Acces permis')
#         break
#     else:
#         print('Parola gresita. mai incercati.')
# else:
#     print('Acccount locked')
#
# i = 0
# while i < 3:
#     passw = input("Introduceti parola:")
#     if passw == "7788":
#         print("Access permis!")
#         break
#     else:
#         print("Parola gresita. Mai incercati.")
#         i += 1
# else:
#     print("PC-ul este blocat pentru urmatoarele 30 minute!!!")

##################################################################

# my_list = ["Masa", 5, "Scaun", 4.5, [5, 6, 7], 8]
#
# for elem in my_list:
#     print("Tipul", elem, "este :", type(elem))
#     if(type(elem) == list):
#         for el in elem:
#             print("    Nivelul 2:", el, "este", type(el))

##################################################################

cuvant = input("introduceti un cuvant fara majuscule:")
x = list(cuvant)
y=x.count(x[0])
print(y)