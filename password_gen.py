import random as rng
import numpy as np
def gen_string(length,nums):
    t=rng.randint(0,length-1)
    h=nums
    string = []
    str=""
    if(nums>length):
        print("invalid input");
        return None
    else:
        for i in range(0,length):
                string.append(chr(rng.randint(97,122)))
        for i in range(0,nums):
             string[t]=chr(rng.randint(48,57))
             t=(t+1)%length
        for i in range(0,length):
             str+=string[i]
    return str
def get_uniq_nums_len(t):
     s=set()
     for i in t:
          if i not in s:
               s.update(i)
     return len(s)
def get_uniq(t):
     s = set()
     k=[]
     for i in t:
          if i not in s:
               s.update(i)
     while s:
          k.append(s.pop())
     return k
def entropy(string):
     entropy=0
     count=0
     t=[]
     l=len(string)
     for i in range(0,l):
          t.append(string[i])
     n=get_uniq_nums_len(t)
     k=get_uniq(t)
     for i in k:
          for j in range(0,l):
               if t[j]==i:
                    count+=1
          entropy+=-1*np.log2(count/l)
     return entropy
print("Enter the number of characters in the password")
a=int(input())
print("Enter the number of numerical values in the password")
b=int(input())
c=gen_string(a,b)
e=entropy(c)
print("Password is ",c," entropy is  ", e)



