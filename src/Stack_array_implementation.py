'''
Created on 5 Mar 2017

@author: Daniele
'''

# last element of the array is the top element of the stack


class Stack_array:

    def __init__(self, n=500):
        self.items = [] # assign value of a list to the stack
        self.size = n # unless otherwise specified the size of the stack is 500

    def length(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.length() == 0
    
    def isFull(self):
        return self.length() >= self.size
    
    def peek(self):
        if self.isEmpty() == True:
            raise ValueError('the stack is empty, I cannot peek')
        else:
            return self.items[0]
    
    def push(self,e):
        self.items.insert(0,e)
            
    def pop(self):
        if self.isEmpty() == True:
            raise ValueError('the stack is empty, I cannot pop any element')
        else:
            poppedItem = self.items[0]
            del self.items[0]
            return poppedItem
            
    def show(self):
        print(self.items)
            
    




