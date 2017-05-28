'''
Created on 5 Mar 2017

@author: Daniele
'''
from src.Stack_array_implementation import *
import time
import matplotlib.pyplot as plt

running_times = []

# Increase size of n in increments. 
for n in range (50, 50000, 500):
    s = Stack_array(1000000)
    # Add n elements to the set.
    for i in range(n):
        s.push(i)

    start = time.time()
    # the operation I will test is get the length of an array, I am expecting O(1) complexity
    print(s.length())
    
    end = time.time()

    run_time = end - start
    print(n, run_time)
    running_times.append(run_time)
# Plot the running times
plt.plot(running_times, 'bx')
plt.xlabel('Size of N (x 1000)')
plt.ylabel('Time')
plt.show()