#Exercise 17
    #given two integers return the sum between the two including the intergers
def sumRange(num1,num2):
    sumnum = 0
    for i in range(num1,num2+1):
        sumnum += i

    return sumnum

print(sumRange(3,6))
