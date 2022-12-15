# continue

my_str = 'abcdef'

for letter in my_str:
    print('before continue')
    if letter == 'd':
        continue #this will stop current itteration
    # if letter == 'f':
    #     break #this will stop for loop
    print(letter)
else:
    print('All is done')

my_number = 0

while my_number < 5:
    print(my_number)
    my_number += 1
else:
    print('all done')