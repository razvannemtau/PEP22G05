# class A():
#     attr1 = 'my_text'
#     attr2 = 10
# a = A()
# # print(a.__repr__())
# print(dir(a))
# # check attribute exists
# print(hasattr(a, "attr1"))
# print(hasattr(a, "attr3"))
#
# # get value from attribute
# print(getattr(a, "attr3", "abcd"))
# print(getattr(a, "attr2", "abcd"))
#
# # setting and attribute
# for i in range(100):
#     setattr(a, f"attr{i}", f"{i+1}")
#
# print(dir(a))
# print(a.attr1)
# print(a.attr2)
#
# print(a.__setattr__("new_attr", "100"))
# # print(a.new_attr)
# print(a.__getattribute__("new_attr"))
#
# # Create object and set attributes from input
# while True:
#     response = input("Dati, va rog, atribut si valoare:")
#     if response == "q":
#         break
#     attr1, bal1 = response.split(",")
#     a.__setattr__(attr1, bal1)
#     print(dir(a))

class A:
    attr_A = 'A'
    custom = 'my custom text'

    def mymethod(self):
        print(self.custom)

class B(A):
    attr_B = 'B'
    custom = 1
class D(A):
    attr_D = 'D'
    custom = 2

class C(B,D,A):
    attr_C = 'C'
    custom = 'my custom 10'

    def __init__(self):
        print("custom attirbute is", self.custom)
        print("custom inherited attirbute is", super().custom)


a = A()
b = B()
c = C()

print(b.attr_B)
print(b.attr_A)
print(c.attr_C)
print(a.custom)
print(c.attr_D)

c.mymethod()