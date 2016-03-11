# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 08:04:46 2016

@author: karl.surmacz
"""

import unittest
from probabilistic_graphical_models import structures

class StructuresTestCase(unittest.TestCase):
    """Tests for 'structures.py'."""
    
    def test_create_induced_subgraph(self):
        node_1 = structures.Node("A")
        node_2 = structures.Node("B")
        node_3 = structures.Node("C")
        edge_1 = structures.Edge(node_1, node_2, True)
        edge_2 = structures.Edge(node_1, node_3, False)
        input_graph = structures.Graph([node_1, node_2, node_3], [edge_1, edge_2])
        actual_output = input_graph.create_induced_subgraph(input_graph, [node_1, node_3])
        
        expected_output = structures.Graph([node_1, node_3], edge_2)
        
        self.assertEqual(actual_outptut, expected_output)