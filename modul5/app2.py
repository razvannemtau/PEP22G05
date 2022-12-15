# nume = input("Introduceti numele:")
# str_note = input("Introduceti notele elevului separate prin virgula:")
# str_note = str_note.replace(" ", "")
# assert str_note, "Nu ai dat nicio nota!"
# note = str_note.split(",")
# lista_note =[]
#
# for nota in note:
#     try:
#         lista_note.append(int(nota))
#     except (ValueError, ZeroDivisionError):
#         print("introduceti note 1-10!")
# print(lista_note)
#
# media = sum(lista_note)/len(lista_note)
# print("media = ", media)
# if media>=5:
#     print(f"{nume} a trecut clasa!")
# else:
#     print(f"{nume} nu a trecut clasa!")
#
# nums = [1,2,3]
# vals = nums
#
# del vals[:]
# print(vals)
# print(nums)
# from modul5 import part2

# def mysplit(strng):
#     new_string = ''
#     for i in strng:
#         if i == ' ':
#             continue
#         else:
#             new_string = new_string + i
#     return new_string
#
# print(mysplit("To be or not to be, that is the question"))
# print(mysplit("To be or not to be,that is the question"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))

