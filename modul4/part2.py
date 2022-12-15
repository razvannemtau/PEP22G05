# Variables in functions

# global variables in functions

# my_var = "Raz"
#
# def print_data():
#     global my_var
#     my_var = 'new name'
#     my_local = 'local'
#     print(f"Global {my_var}")
#     def new_print_data():
#         nonlocal my_local
#         my_local = 'modified local'
#         print(f'In second function local {my_local}')
#         print(f'In second function {my_var}')
#     new_print_data()
#     print(f'local var in first function {my_local}')
#
# print(f"outside Global {my_var}")
# print_data()

# """
# Crate app that is able to respond with the provided name
# Hi Bob,
# >>> My name is Jhon
# Hi Jhon
# How is the weather
# >>> The weather is cold
# For Jhon weather is cold
# All of this will be in a function .
# """


def robot():
    name = 'Bob'
    def functie():
        nonlocal name
        print('Hi', name)
        name = input('My name is ')
        print('Hi ', name)

    functie()

    def weather():
        vremea = input('how is the weather?')
        print("for", name, "the weather is", vremea)
    weather()
robot()



