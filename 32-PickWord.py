#import random
#words_lst = []

'''
with open("sowpods.txt", "r") as f:
    words = f.readline()
    while words:
        words_lst.append(words)
        words = f.readline()



print(words_lst)
'''

import random 

lst_words = []
with open('sowpods.txt', 'r') as f:
  words_read = f.readline()
  while words_read:
    lst_words.append(words_read)
    words_read = f.readline()

print(lst_words)
print('Word selected: ' + str(lst_words[random.randint(0,len(lst_words)-1)])) 