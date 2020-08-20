#Exercise 11
    #Write a recursive function that given a list of numbers returns the sum

def recursiveSumIt(numList):
    
    if len(numList) == 2:
        numList[0]+ numList[1]
        return numList[0]+ numList[1]

    print(numList)
    return numList.pop()+ recursiveSumIt(numList)
    
    #return recursiveSumIt(numList)

print(recursiveSumIt([1,2,3,432]))