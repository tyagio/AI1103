# -*- coding: utf-8 -*-
"""assignment6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gk_ALPhJy9IRLMrrEOLVuwfqHKsHdY8V
"""

import numpy as np
sample=500000
true=0
all=0
#all denotes cases when X<2Y
#true denotes cases when Y<X<2Y 
x = np.random.uniform(0,4,size=sample)
y = np.random.uniform(0,4,size=sample)
for i in range(sample):
    if(x[i]<2*y[i] and x[i]>y[i]):
      true+=1
      all+=1  
    elif(x[i]<(2*y[i])):
      all+=1  
answer=true/all              
print("Calculated probability is ",answer)     
print("Theoretical probability is 1/3 or 0.333...")
print("percentage error between calculated and theoretical is {}%".format(300*(answer-1/3)))
print("Calculated and theoretical probability differ by a very small extent,hence simulation correct")