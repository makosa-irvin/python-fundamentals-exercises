#Exercise 5
    #Determine the prime number

#ensure user enters an integer
try:
    #user inputs
    num = int(input('Enter an integer less than 50 >'))
    if num > 50:
        print('The integer is more than 50')

    else:
    #to check if a number is prime divide by all numbers that are less than or equal to squareroot of 50
        sqr50 = 50 ** .5
        is_prime = True

        for i in range(2,int(sqr50)+1):
            if num % i == 0:
                is_prime = False

        if is_prime:
            print(num,'is prime.')

        else:
            print(num,'is not prime')



except ValueError:
    print('Please enter an integer below 50')