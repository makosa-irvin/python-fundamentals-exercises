1#Exercise 1
    #Program that prints prime numbers less than a given number
        #Should use nested loops
            #Outer loop for all numbers 2 to n
            #inner loop for the list of prime numbers
try:
    n = int(input('Enter a number >'))

    #Prime numbers list
    prime_list = [2]

    #nested for loops
    for i in range(2,n):#outer loop runs through 2 to given number
        is_prime = True
        for j in prime_list:#inner loop runs through the list of prime numbers this makes it possible to divide number with numbers in the prime list
            
            if len(prime_list)==0:
                prime_list.append(i)

            elif i % j == 0:
                is_prime = False

        if is_prime:
            print(i)
            prime_list.append(i)

    print(prime_list)

except ValueError:
    print('You did not enter an integer')

