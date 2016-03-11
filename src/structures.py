# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 18:55:58 2016

@author: karl.surmacz
"""

class Graph():
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        
    def create_induced_subgraph(self, nodes):
        import sets        
        subgraph_edges = []   
        subgraph_nodes = [];
        for graph_edge in self.edges:
            this_edge_nodes = [graph_edge.start_node, graph_edge.finish_node]          
            if set(this_edge_nodes) == set(nodes):
                subgraph_edges = [subgraph_edges, graph_edge]    
                subgraph_nodes = [subgraph_nodes, this_edge_nodes]
                subgraph_nodes = set(subgraph_nodes)
                
        subgraph = Graph(subgraph_nodes, subgraph_edges)
        return subgraph
        
class Edge():
    def __init__(self, start_node, finish_node, is_two_way):
        self.start_node = start_node
        self.finish_node = finish_node
        self.is_two_way = is_two_way
        
class Node():
    def __init__(self, name):
        self.name = name
        
        