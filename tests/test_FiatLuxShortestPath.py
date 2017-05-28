'''
Created on 12 Mar 2017

@author: Daniele
'''
import sys

from src.FiatLuxShortestPath import *


def test(did_pass):
    line_num = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(line_num)
    else:
        msg = ("Test at line {0} FAILED.".format(line_num))
    print(msg)
        


    
def test_simple():
    
    board = Board("world1.txt") 
    
    test(board.where_is_robot() == [7,0])
    test(board.is_feasible(6, 0) == True)
    test(board.is_feasible(5, 0) == True)
    test(board.is_feasible(-1, 0) == False)
    test(board.is_feasible(-1, -1) == False)
    test(board.is_feasible(1, 8) == False)
    test(board.is_feasible(8, 1) == False)
    board.move_robot(6, 0)
    test(board.is_feasible(6, 0) == True)
    test(board.where_is_robot() == [6,0])
    test(board.goal_reached() == False)
    board.move_robot(0, 7)
    test(board.goal_reached() == True)
    
    
test_simple()
