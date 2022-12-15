#functions

# # 3! = 1*2*3
# def factorial(number):
#     print(number)
#     result = 1
#     for i in range(1, number+1):
#         result *= i
#     return result
#
# factorial(10)
# result = factorial(10)
# print('result', result)

# def factorial(number, limit):
#     print(number)
#     result = 1
#     for i in range(1, number+1):
#         if result > limit:
#             return result
#         result *= i
#     return result
#
# result = factorial(100, 1000)
# print('result', result)

# Variable number of arguments

def arguments(*args):
    print(args)
