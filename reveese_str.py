#!/usr/bin/env python
# coding: utf-8

# In[3]:


strlist = []
palindrome = []
word='0'

def reveese_str(string):
    return string[::-1]

while word != '':
    word = input('請輸入字串，當您輸入0就代表結束')
    strlist.append(word)
    if word == '0':
        break
    if word == reveese_str(word):
        palindrome.append(word)
        continue
strlist.remove('0')
print('顯示清單內容:\n'+ str(strlist))
print('符合回文的字串為:\n' + str(palindrome))

