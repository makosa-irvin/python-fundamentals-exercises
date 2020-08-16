#Exercise 7
    #Convert 8 bit binary number to decimal equivalent
        #The weight of each digit increases by a factor of 2
        #Then add the values when the binary digit is 1
    
#user inputs
num_bin = input('Enter the binary representation >')



#check if it is negative
    #ASSUMPTION: I understand that having '1' on the most left side doesn't mean it is neccessarily negative
                #For instance in 8 bit, 1111101 can represent -3 or 253
                #Because I want to rep both positive and negative we will assume negative if '1' is in the most left side
    #One must get the 2's complement of the binary number
    #This is by reversing all 1's and 0's and then adding 1 to result
    
if len(num_bin) == 8 and num_bin[0] == '1':
    #result = -result



    
    num_bin_rev = []

    #to loop inorder to change 1 to 0 and 0 to 1
    for i in num_bin:

        if i == '1':
            num_bin_rev += '0'

        elif i == '0':
            num_bin_rev += '1'

    #adding one
    idx = len(num_bin_rev)-1

    while idx >= 0:

        if num_bin_rev[idx] == '0':
            num_bin_rev[idx] = '1'

            break


        elif num_bin_rev[idx] == '1':
            num_bin_rev[idx] = '0'

            idx -= 1

    num_bin2 = ''.join(num_bin_rev)

    #coverts to the  binary number of the postive value of decimal equivalent
    numbin_reverse = num_bin2[::-1] #reverses the list thus last item becomes first and vice versa
    result = 0

    for idx in range(len(numbin_reverse)):
        if numbin_reverse[idx] == '1':
            result += 2 ** idx

    result = -result

else:
    #coverts to the  binary number of the postive value of decimal equivalent
    numbin_reverse = num_bin[::-1]#reverses the list thus last item becomes first and vice versa
    result = 0

    #coverts to the  binary number of the postive value of decimal equivalent
    for idx in range(len(numbin_reverse)):
        if numbin_reverse[idx] == '1':

            result += 2 ** idx

print('The base 10 equivalent of',num_bin, 'is', result)

