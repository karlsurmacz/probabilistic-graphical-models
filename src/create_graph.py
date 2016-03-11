# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 19:04:47 2016

@author: karl.surmacz
"""
import structures

if __name__ == "__main__":
    node_1 = structures.Node("A")
    node_2 = structures.Node("B")
    node_3 = structures.Node("C")
    edge_1 = structures.Edge(node_1, node_2, True)
    edge_2 = structures.Edge(node_1, node_3, False)
    
    graph = structures.Graph([node_1, node_2], [edge_1, edge_2])
    
    graph.create_induced_subgraph([node_1,node_2])