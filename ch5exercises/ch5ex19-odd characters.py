#Exercise 19
    #Given a string return the odd characters of a string based on the index

def oddCharacters(word):
    oddList = []
    for i in range(1,len(word)):
        if i%2 != 0:
            oddList.append(word[i])

    oddStr = ''.join(oddList)
    return oddStr


print(oddCharacters('Hallo'))
