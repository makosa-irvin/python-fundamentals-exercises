#Exercise 18
    #Given a sentence reverse the words

#top down approach
#part 1 - Assemble already reversed sentences
def reverseWords(sentence):
    st = []
    s_list = sentence.split()
    for word in s_list:
       word = reverse(word)
       st.append(word)

    st2 = ' '.join(st)
    return st2

#part 2 - Reverse the word
def reverse(word):
    w_list = [i for i in word]
    w_listR = w_list[::-1]

    word_rev = ''.join(w_listR)
    return word_rev 

s = input('Enter a sentence >')
print(reverseWords(s))