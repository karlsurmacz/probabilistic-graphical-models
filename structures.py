# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 18:55:58 2016

@author: karl.surmacz
"""

class Graph():
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        
class Edge():
    def __init__(self, start_node, finish_node, is_two_way):
        self.start_node = start_node
        self.finish_node = finish_node
        self.is_two_way = is_two_way
        
class Node():
    def __init__(self, name):
        self.name = name
        
        