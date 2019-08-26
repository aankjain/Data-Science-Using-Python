#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1. Write a program which will find factors of given number and find whether the factor is even or odd.
#Hint: Use Loop with if-else statements
def factors(x):
    print('Factors of',x,'are')
    for i in range(1,x+1):
        if x % i == 0:
            if i % 2 == 0:
                print(i,'is even number')
            else:
                print(i,'is odd number')
factors(50)


# In[5]:


#2. Write a code which accepts a sequence of words as input and prints the words in a sequence
#after sorting them alphabetically.
#Hint: In case of input data being supplied to the question, it should be assumed to be a console input.

my_str = "Welcome to Python"
words = my_str.split()
words.sort()
print("The sorted words are:")
for word in words:
   print(word)


# In[8]:


#3. Write a program, which will find all the numbers between 1000 and 3000 (both included) 
#such that each digit of a number is an even number. The numbers obtained should be printed 
#in a comma separated sequence on a single line.
#Hint: In case of input data being supplied to the question, it should be assumed to be a console input.
#Divide each digit with 2 and verify is it even or not.

items = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        items.append(s)
print( "-".join(items))


# In[10]:


#4. Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose if the entered string is: Python0325
#Then the output will be:
#LETTERS: 6
#DIGITS:4
#Hint: Use built-in functions of string.

s = input("Input a string ")
d=l=0
for i in s:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)


# In[11]:


#5. Design a code which will find the given number is Palindrome number or not.
#Hint: Use built-in functions of string.

s = input('Enter a String ')
s1 = ''.join(reversed(s))
if s == s1:
    print('Input is a palindrome')
else:
    print('Input is not a palindrome')


# In[ ]:




