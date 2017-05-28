'''
Created on 5 Mar 2017

@author: Daniele
'''
from src.linked_list import *

# with linked list its easier to consider the head as the top element of the stack (unlike the array in python)



class Stack_linkedList(LinkedList):

    def __init__(self, n=500):
        LinkedList.__init__(self,node=None)
        self.size = n # unless otherwise specified the size of the stack is 500

    def length(self):
        current = self.head()
        count = 0
        while not (current is None):
            current = current.get_next()
            count +=1
        return count
    
    def isEmpty(self):
        return self.head() == None
    
    def isFull(self):
        return self.length() == self.size
    
    def peek(self):
        if self.isEmpty() == True:
            raise ValueError('the stack is empty, I cannot peek')
        else:
            return self.head()
    
    def push(self,e):
        self.add_head(Node(e))
            
    def pop(self):
        if self.isEmpty() == True:
            raise ValueError('the stack is empty, I cannot pop any element')
        else:
            poppedItem = self.head()
            self.remove_head()
            return poppedItem


        
        