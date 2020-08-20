#Exercise 14
    #Given an integer return a list of factors of the integers

def factors(num):
    factors_list = []
    for i in range(1,num):
        if num%i == 0:
            factors_list.append(i)

    return factors_list

#Exercise 15
    #return sum of all factors of an integer 

def sumFactors(num):
    numList = factors(num)
    sumnum = 0
    for i in numList:
        sumnum+= i

    return sumnum

#Exercise 16
    #given an integer returns true if sum of its factors excluding itself is the number itself

def isPerfect(num):
    sumnum = sumFactors(num)
    return sumnum == num

    
print(isPerfect(8))
