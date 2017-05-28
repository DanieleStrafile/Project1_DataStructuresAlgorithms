'''
Created on 5 Mar 2017

@author: Daniele
'''
import time
import matplotlib.pyplot as plt
from src.Stack_linkedList_implementation import *

running_times = []

# Increase size of n in increments. 
for n in range (5, 50000, 183):
    s = Stack_linkedList(100000)
    # Add n elements to the set.
    for i in range(n):
        s.push(i)

    start = time.time()
    # the operation I will test is getElementAtRank(n // 2 (integer division)). I am expecting O(1) complexity
    for j in range(n//2):
        s.pop()
    x = s.peek()
    end = time.time()

    run_time = end - start
    print(n, run_time)
    running_times.append(run_time)
# Plot the running times
plt.plot(running_times, 'bx')
plt.xlabel('Size of N (x 1000)')
plt.ylabel('Time')
plt.show()