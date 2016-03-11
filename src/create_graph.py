# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 19:04:47 2016

@author: karl.surmacz
"""
import structures

if __name__ == "__main__":
    node_1 = structures.Node("A")
    node_2 = structures.Node("B")
    edge = structures.Edge(node_1, node_2, True)
    
    graph = structures.Graph([node_1, node_2], edge)