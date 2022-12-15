cappucino = 4
espresso = 3.5
print( f"1. cappucino...{cappucino} lei")
print( f"2. Espresso... {espresso} lei")
# optiune = input("ce optiuni alegeti? [1,2]").strip()

# optiune = int(input('select 1 to 2'))
# while not (1 <= optiune < 3):
#     optiune = int(input('select 1 to 2'))

bancnota = int(input("introduceti o bancnota [5 lei, 10 lei]"))
print(optiune)

while True:
    a = int(input('Ce optiune alegeti? [1,2]'))
    if(a==1 or a==2):
        break

#
if optiune == 1:
    rezultat = bancnota - cappucino
elif optiune == 2:
    rezultat = bancnota - espresso
else:
    rezultat = bancnota
print(f"vei primi restul de {rezultat}")

