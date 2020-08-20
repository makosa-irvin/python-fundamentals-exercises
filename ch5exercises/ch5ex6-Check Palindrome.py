#Exercise 6
    #Write a func that checks if string  is a palindrome

def isPalindrome(word):
    lst = []
    
    for i in word:
        
        lst.append(i)
    
    #reverse the list
    lst2 = lst[::-1]

    if lst == lst2:
        return True
    return False
    

w = input('Enter a word >')
print(isPalindrome(w.lower()))