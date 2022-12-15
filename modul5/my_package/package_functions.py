def factorial(limit):
    result = 1
    for i in range(1, limit + 1):
        result *= i
    return result

print(__name__)
if __name__ == "__main__":
    print(__name__)
    print("print from my_functions", factorial(5))

my_imported_var = 6

import random

def play():
    states ={'p': 'piatra',
             'f': 'foarfeca',
             'h': 'hartie'
             }
    user = input("'p = piatra, h = hartie, f=foarfeca")
    if user == 'q':
        print('L O O O S E R')
        quit()