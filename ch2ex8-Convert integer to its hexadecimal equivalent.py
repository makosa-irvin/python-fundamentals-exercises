#Exercise 8
    #Convert number to hexadecimal
#user input
num = int(input('Please enter a number >'))


remainder_list = ''
#remainders
while num > 0:
    rem = int(num % 16)

    if rem == 10:
        rem = 'a'

    elif rem == 11:
        rem = 'b'

    elif rem == 12:
        rem = 'c'

    elif rem == 13:
        rem = 'd'

    elif rem == 14:
        rem = 'e'

    elif rem == 15:
        rem = 'f'


    remainder_list = str(rem) + remainder_list
    num = num // 16

#print(hex(255))
print('0x{}'.format(remainder_list))
