'''
Created on 5 Mar 2017

@author: Daniele

'''
import re
import urllib.request

from src.Stack_linkedList_implementation import Stack_linkedList


class Robot:
    
    coords = []
    def __init__(self,coord):
        self.coords = coord
        
        
class Board:
    
    def __init__(self,url):
        self.var = self.create_world(url) 
        self.world = self.var[0] 
        self.robot = Robot(self.var[1])
        self.goal = self.var[2]
        self.current_path = Stack_linkedList()
     
     
    
    def read_uri(self,uri):
        if uri.startswith('http'):
            # case where file is on the net
            req = urllib.request.urlopen(uri)
            buffer = req.read().decode('utf-8')
            lines = buffer.splitlines()
            return lines
        else:
            ## case where file is local file
            buffer = open(uri).readlines()
            return buffer
                # process line
    #for robot
    def matrix(self,row,column):
        return [ [0]*column for _ in range(row) ]
    

    def create_world(self,link_file):
        buffer = self.read_uri(link_file)
        num_lines = (sum(1 for line in buffer))-1
        # check that line contains one of the three possible commands at the beginning
        for i, line in enumerate(buffer):#
            if i==0:
                world_coordinates = re.findall('-?\d+', line)
                world_coordinates = [int(x) for x in world_coordinates]
                world = self.matrix(world_coordinates[0],world_coordinates[1])
            elif i == num_lines-1:
                robot_coordinates = re.findall('-?\d+', line[4:])
                robot_coordinates = [int(x) for x in robot_coordinates]
            elif i == num_lines:
                goal_coordinates = re.findall('-?\d+',line)
                goal_coordinates = [int(x) for x in goal_coordinates]
            else:
                wall_coordinates = re.findall('-?\d+', line)
                wall_coordinates = [int(x) for x in wall_coordinates]
                world[wall_coordinates[0]][wall_coordinates[1]] = 1
        return [world, robot_coordinates, goal_coordinates]   
        
        
    def where_is_robot(self):
        return self.robot.coords    
        
    def is_feasible(self,row,column):
        # not possible to go out of the map, # 1 is a wall, 2 is flagged
        if  row < 0 or column < 0 or row >= len(self.world) or column >= len(self.world[0]):
            return False
        # the robot is moving horizontally or vertically or does not move
        else:
            return True
    
    # move robot only if path is feasible
    def move_robot(self,row,column):
        #move robot
        self.robot.coords = [row,column] 
            
            
    
    def goal_reached(self):
        if self.robot.coords == self.goal:
            print("goal reached")
            return True
        else:
            print("goal not reached")
            return False  
        
        
    def find_path(self,element,robot1,robot2):
        
        #push element by default
        self.current_path.push(element)
        #if the instructions are invalid
        if self.is_feasible(robot1, robot2) == False:
            self.current_path.pop()
            return False
        
        #if we reached the goal 
        if [robot1,robot2] == self.goal:
            self.current_path.__repr__()
            print("found the goal")
            return True
        # if we are not on a good path ( bad path is 1 for wall and 2 for already gone there)
        if (self.world[robot1][robot2] != 0):
            self.current_path.pop()
            return False
        
        #flag
        self.world[robot1][robot2] = 2
        
        # if we can move east
        if self.find_path([robot1,robot2+1],robot1,robot2+1) == True:
            return True
        # if we can move south
        if self.find_path([robot1+1,robot2],robot1+1,robot2) == True:
            return True
        # if we can move north
        if self.find_path([robot1-1,robot2],robot1-1,robot2) == True:
            return True
        # if we can only move west
        if self.find_path([robot1,robot2-1],robot1,robot2-1) == True:
            return True
    
b = Board("world1.txt") 
b.find_path("Start", b.where_is_robot()[0],b.where_is_robot()[1])     