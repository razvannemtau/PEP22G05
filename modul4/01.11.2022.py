# PC1 = 'admin1' , : passme1
# PC2 = 'admin2', : passme2
# # PC3 = 'admin3', : passme3
#
# def calculator():
#
#     data = {}
#
#     for i in range(1,4):
#         user = input(f'user pc {i}:')
#         password = input(f'password for pc {i}')
#         data[user] = password
#     for key, value in data.items():
#         print(f'{key} ---> {value}')
# calculator()
#
# hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
#
# # Step 1: write a line of code that prompts the user
# # to replace the middle number with an integer number entered by the user.
# middle_nr = len(hat_list) // 2
# hat_list[middle_nr] = int(input("replace the middle nr"))
# # Step 2: write a line of code that removes the last element from the list.
# del hat_list[-1]
# # Step 3: write a line of code that prints the length of the existing list.
# print('list lenght', len(hat_list))
# print(hat_list)
import random


# beatles = []
#
# beatles.append('John Lennon')
# beatles.append('Paul McCartney')
# beatles.append('George Harriso')
# print("Step 1:", beatles)
#
# for member in range(2):
#     member = input('add member')
#     beatles.append(member)
# print("Step 2:", beatles)
#
# for member in range(2):
#     del beatles[-1]
# print("Step 3:", beatles)
#
# beatles.insert(0, 'Ringo Star')
# print("Step 4:", beatles)
#
# # step 5
# print("Step 5:", beatles)
#
#
# # testing list legth
# print("The Fab", len(beatles))
import random
#
# def guess(x):
#     random_number = random.randint(1,x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'Guess a number between 1 {x}'))
#         print(guess)
#         if guess < random_number:
#             print('too low')
#         elif guess > random_number:
#             print('too high')
#     print(f'correct {random_number}')
#
# guess(10)

# def computer_guess(x):
#     low = 1
#     high = x
#     feedback  = ''
#     while feedback != 'c':
#         if low != high:
#             guess = random.randint(low, high)
#         else:
#             guess = low
#         guess = random.randint(low, high)
#         feedback = input(f'is {guess} too high (H), too low (L), or correct (C)' )
#         if feedback == 'h':
#             high = guess -1
#         elif feedback == 'l':
#             low = guess + 1
#     print(f'yey!{guess}')
#
# computer_guess(1000)

# def play():
#     user = input("'r for rock, p = paper, s = scissors")
#     computer = random.choice(['r', 'p', 's'])
#
#     if user == computer:
#         return 'tie'
#     if is_win(user, computer):
#         return 'You win!'
#     return 'you lost!'
#
# def is_win(player, opp):
#     # r>s, s>p, p>r
#     if(player == 'r' and opp == 's') or (player == 's' and opp == 'p') or (player == 'p' and opp == 'r'):
#         return True
#
# print(play())


# def message(a, b, c):
#     print("Enter a value: ")
# result = []
# for i in range(3):
#     message()
#     a = int(input())
#     print(a)
#     result.append(a)
#     print(result)
#
# print(sum(result))

# num = 13
# print(num)
# for i in range(2, num):
#     if num % 2 == 0:
#         print('is not prime')
#         break
#     else:
#         (print(num, 'is prime'))
#         break

# 1 American mile = 1609.344 metres;
# 1 American gallon = 3.785411784 litres.

print(20/100 * 100/1.609344)

# def liters_100km_to_miles_gallon(liters):
#     liters / 100 * 1.609344
#
# def miles_gallon_to_liters_100km(miles):
# #
# # Write your code here
# #
#
# print(liters_100km_to_miles_gallon(3.9))
# print(liters_100km_to_miles_gallon(7.5))
# print(liters_100km_to_miles_gallon(10.))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))