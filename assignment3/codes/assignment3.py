import numpy as np
import random
sample=1000
n=100
true=0
for i in range(sample):
  sum=0
  for j in range(n*n):
    sum+=random.choice([1,-1])
  if(sum>n/10):
    true+=1
print("there might be some error as theoretical answer when n approaches infinity")
print("Code might take some time to execute")
print("this is approximated answer from simulation",true/sample)
print("Theoretical answer is 0.46")