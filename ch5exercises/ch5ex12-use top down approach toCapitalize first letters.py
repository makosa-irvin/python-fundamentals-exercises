#Exercise 5
    #Capitalize first letter of every word

    #using top down approach

#part one
def capitalized(sentence):
    st = []
    s_list = sentence.split(' ')

    for word in s_list:
        word = capitalize1stletter(word)
        st.append(word)
    
    st2 = ' '.join(st)
    return st2

    
#part 2 -->change first letter to capital
def capitalize1stletter(string):
    
    string_list = [i for i in string]
    
    if is1stcapital(string) == True:
        return string

    else:
        
        string_list[0]= string_list[0].upper()
        
        string = ''.join(string_list)
        return string

#part 3 -->check if first letter is capital
def is1stcapital(string):
    string_list = [i for i in string]
    
    return string_list[0].isupper()





s= input('Enter a sentence >')
print (capitalized(s))
