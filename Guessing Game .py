#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Guessing Game
import random
N1= random.randint(1,100)
Number= int(input("Guess the number:"))
if Number == N1:
    print("Congratualations! You won!")
elif  Number <1:
    print("Too low!")
elif Number >100:
    print("Too high!")
else:
    print("Better luck next time !")


# In[ ]:




