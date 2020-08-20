#Exercise 13
    #When using bottom down approach we start the the smallest deetails as we build to a bigger picture

#part one-->check if first letter is capital
def is1stcapital(string):
    string_list = [i for i in string]
    
    return string_list[0].isupper()

#part 2 -->We then capitalize each first letter
def capitalize1stletter(string):
    
    string_list = [i for i in string]
    
    if is1stcapital(string) == True:
        return string

    else:
        
        string_list[0]= string_list[0].upper()
        
        string = ''.join(string_list)
        return string

#part 3 -->we then assembly each word to make a new sentence with first letter capitalized
def capitalized(sentence):
    st = []
    s_list = sentence.split(' ')

    for word in s_list:
        word = capitalize1stletter(word)
        st.append(word)
    
    st2 = ' '.join(st)
    return st2

s= input('Enter a sentence >')
print (capitalized(s))
