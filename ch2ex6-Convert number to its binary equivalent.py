#Exercise 6
    #Convert decimal number to its binary equivalent
        #This is done by accumulating remainders of the number when divided by 2

#user input
num = int(input('Please enter a number >'))

print(bin(num))
remainder_list = ''
#remainders
while num > 0:
    rem = int(num % 2)
    remainder_list = str(rem) + remainder_list
    num = num // 2

print(remainder_list)
