#generate prime numbers
from random import choice

def primes(limit):
    result = []
    for i in range(2, limit):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result.append(i)
    return result
print(primes(256))

# get 2 random prime numbers from list. Second number is smaller than first

my_primes = primes(255)

# def get_primes(list_primes):
#     while True:
#         base = choice(list_primes)
#         if base < 129:
#             continue
#         else:
#             break
#         print(base)
#         return 1,2
# # bigger    #smallerr
# base,       prime =    get_primes(my_primes)

def get_primes(list_primes):
    base_set = []
    for i in list_primes:
        if i >= 129:
            base_set.append(i)
    base = choice(base_set)
    print(base)
    return 1,2
# bigger    #smallerr
base,       prime =    get_primes(my_primes)

def generate_local_secret():
    result = choice(range(2, base))
    return result

secret1 = generate_local_secret(base)
secret2 = generate_local_secret(base)
print(secret1)
print(secret2)

