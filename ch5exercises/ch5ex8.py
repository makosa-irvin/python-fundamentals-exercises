#Exercise 8
    #Write a func given two list of same length creates a tuple

def zip(numList1,numList2):
    if len(numList1) == len(numList2):
        tupleList = []
        for i in range(len(numList2)):
            tup = (numList1[i],numList2[i])
            tupleList.append(tup)
        
        return tupleList

    else:
        print('The lists are not of the same length')

print(zip([1,2,3],[4,5,6]))

#Exercise 9
    #Write a func that reverses Exercise 8

def unzip(tupleList):
    numList1 = []
    numList2 = []

    for i in tupleList:
        numList1.append(i[0])
        numList2.append(i[1])

    return numList1,numList2
def main():

    print(unzip([(1,4),(2,5),(3,6)]))

if if __name__ == "__main__":
    main()
