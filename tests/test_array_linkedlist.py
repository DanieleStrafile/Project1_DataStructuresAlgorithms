'''
Created on 5 Mar 2017

@author: Daniele
'''

'''
Created on 5 Mar 2017

@author: Daniele
'''
import unittest
from src.Stack_array_implementation import *
from src.Stack_linkedList_implementation import *

class TestStackArray(unittest.TestCase):
    
    # check that length of array is = 0 when created
    def test_invalid1(self):
        s=Stack_array()
        l = s.length()
        self.assertEqual(l, 0)
        
        
    # check that isEmpty returns True when empty
    def test_invalid2(self):
        s=Stack_array()
        self.assertTrue(s.isEmpty())
        
    # check that isEmpty returns False when list is not empty. 
    def test_invalid3(self):
        s=Stack_array()
        s.push("e")
        self.assertFalse(s.isEmpty())
    
        # check that isFull returns False when list is not full
    def test_invalid4(self):
        s=Stack_array()
        self.assertFalse(s.isFull())
        
    # check that isFull returns False when list is not full
    def test_invalid5(self):
        s=Stack_array()
        for i in range(0,500):
            s.push(i)
        self.assertTrue(s.isFull())
        
    # check that pop returns the top element in the stack
    def test_invalid6(self):
        s=Stack_array()
        for i in range(0,500):
            s.push(i)
        self.assertEqual(s.pop(), 499)
        
    # check that pop actually removed the top element
    def test_invalid7(self):
        s=Stack_array()
        array = []
        for i in range(0,500):
            s.push(i)
            array += [i]
        self.assertEqual(s.pop(), array.pop())
        
        # check that peek returns the top element in the stack
    def test_invalid8(self):
        s=Stack_array()
        for i in range(0,500):
            s.push(i)
        self.assertEqual(s.peek(), 499)
        
        # check that length of array is = 5 after inserting 5 elements
    def test_invalid9(self):
        s=Stack_array()
        for i in range(0,5):
            s.push(i)
        l = s.length()
        self.assertEqual(l, 5)
    
class TestStackLinkedList(unittest.TestCase):
    
    # check that length of array is = 0 when created
    def test_invalid1(self):
        s=Stack_linkedList()
        l = s.length()
        self.assertEqual(l, 0)
        
        
    # check that isEmpty returns True when empty
    def test_invalid2(self):
        s=Stack_linkedList()
        self.assertTrue(s.isEmpty())
        
    # check that isEmpty returns False when list is not empty. 
    def test_invalid3(self):
        s=Stack_linkedList()
        s.push("e")
        self.assertFalse(s.isEmpty())
    
        # check that isFull returns False when list is not full
    def test_invalid4(self):
        s=Stack_linkedList()
        self.assertFalse(s.isFull())
        
    # check that isFull returns False when list is not full
    def test_invalid5(self):
        s=Stack_linkedList()
        for i in range(0,500):
            s.push(i)
        self.assertTrue(s.isFull())
        
    # check that pop returns the top element in the stack
    def test_invalid6(self):
        s=Stack_linkedList()
        for i in range(0,500):
            s.push(i)
        self.assertEqual(str(s.pop()),"node: " + str(499))
        
        
        # check that peek returns the top element in the stack
    def test_invalid7(self):
        s=Stack_linkedList()
        for i in range(0,500):
            s.push(i)
        self.assertEqual(str(s.peek()),"node: " + str(499))
        
    # check that length of linkedlist is = 5 after inserting 5 elements
    def test_invalid9(self):
        s=Stack_linkedList()
        for i in range(0,5):
            s.push(i)
        l = s.length()
        self.assertEqual(l, 5)
        
        
        
        
        
        
        
if __name__ == "__main__":
    unittest.main()
        