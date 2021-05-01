#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:38:54 2021

@author: ishiyamaryo

A agent search some points in a graph.
If there is not point around a agent, it stop moving.
Around means that left and right, top and bottom in a list ,so a agent can view there.
This study purpose is how a agent decrease the remaining point in the giving graph.  
"""

N = 10

graph = [[0,1,0,0,1],
         [0,0,1,0,0],
         [1,0,0,0,1],
         [0,0,1,0,0],
         [1,1,0,1,0]]
    
def line():
    print("------------\n")

class mas_test:
    
    def __init__(self, state, next_state, get, s):
        self.state = state
        self.next_state = next_state
        self.get = get
        self.s = s
        self.x = 0
        self.y = 0
        
    def pr(self):
        print("\n\nThis is my data\n> state: %d \n> next_state: %d \n> get: %d\n" % (self.state, self.next_state, self.get))
        self.hr_pr()
        
    def hr_pr(self):
        print("I'm here now \n -> (x ,y) = (%d, %d)" %(self.x,self.y))
    
    def learn_yoko(self,num,graph):
        self.s = sum(graph[num])
        if(self.s > 0):
            print("\nI find ... >> y = %d" % num )
        return self.s
    
    def learn_tate(self,num,graph):
        self.s = 0
        for i in range(len(graph)):
            self.s += graph[i][num] 
            
        if(self.s > 0):
            print("\nI find ... >> x = %d" % num )
        return self.s
        
    def here(self, x ,y):
        self.x = x
        self.y = y
    
    def move_yoko(self,graph):
        for i in range(len(graph)):
            if(graph[self.y][i] != 0):
                self.here(i, self.y)
                self.get += graph[self.y][i]
                graph[self.y][i] = 0
                
                print("\nI find points!")
                self.hr_pr()
                break
    
    def move_tate(self,graph):
        for i in range(len(graph)):
            if(graph[i][self.x] != 0):
                self.here(self.x, i)
                self.get += graph[i][self.x]
                graph[i][self.x] = 0
                
                print("\nI find points!")
                self.hr_pr()
                break
            
    def ch(self, opp):
        self.state = opp.state
        self.next_state = opp.next_state
        self.get = opp.get
        self.x = opp.x
        self.y = opp.y
        
    def gr_pr(self, graph):
        #print(graph)
        for a in graph:
            print(*a)
            
    def action_yoko(self,graph):
        count = 0
        while(True):
            if(self.learn_yoko(self.y, graph) == 0):
                print("\nThere ins't any more! (yoko)")
                #break
                return count
            else:   
                self.move_yoko(graph)
                count += 1
    
    def action_tate(self, graph):
        count = 0
        while(True):
            if(self.learn_tate(self.x, graph) == 0):
                print("\nThere ins't any more! (tate)")
                #break
                return count
                
            else:   
                self.move_tate(graph)
                count += 1
    
    def count(self, graph):
        self.total = 0
        for i in range(len(graph)):
            self.total += sum(graph[i])
        print("\nTotal >> %d " % self.total)
        return self.total
        
    def next_x(self,graph):
        self.state += 1
        if(self.x == len(graph) - 1):
            self.x = 0
        else:
            self.x += 1
    
#(state, next_state, t, s):  
agent1 = mas_test(0,0,0,0)

#agent2 = mas_test(1,0,0,0)

#deback
agent1.pr()
agent1.here(0,3)

while(True):
    line()
    yoko = agent1.action_yoko(graph)
    tate = agent1.action_tate(graph)
    line()
    agent1.gr_pr(graph)
    if(agent1.count(graph) == 0):
        break
    if(yoko == 0 and tate == 0):
        agent1.next_x(graph)
    line()
    
agent1.pr()
        

