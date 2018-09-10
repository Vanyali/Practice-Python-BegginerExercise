'''
wrd = input("Please enter a word.\n")
wrd = str(wrd).lower()
rvs=wrd[::-1]
if rvs == wrd:
    print("This word is palindrome.")
else:
    print("This is not a palindrome.")
'''

#Using fucntion

def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word)-1-i]
    return x


word = input("Give me a word!\n")
x = reverse(word)

if x == word:
    print("This is palindrome!")
else:
    print("This is not palindrome!")



        
    
        
            

