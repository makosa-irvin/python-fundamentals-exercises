#Exercise 5
    #Write a function given a list of integers returns a new list of those which are even

def allEvens(numList):
    evens_list = []

    for i in numList:
        if isEven(i):
            evens_list.append(i)

    return evens_list
#Exercise 4
    #Function that returns true if number is even
def isEven(num):
    return num % 2 == 0

print(allEvens([2,34,42,632,32,563,633,221]))