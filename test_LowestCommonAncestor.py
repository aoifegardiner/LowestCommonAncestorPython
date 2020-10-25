# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 10:28:55 2020

@author: aoife
"""
        
import unittest
import LowestCommonAncestor

class TestLca(unittest.TestCase):

    def test_emptyTree(self):
        self.assertEqual(LowestCommonAncestor.findLCA(None, None, None), None)
        
    def test_tree(self):
        self.assertEqual(LowestCommonAncestor.findLCA(LowestCommonAncestor.root, 2, 3).key, 1)

    def test_leftTree(self):
        self.assertEqual(LowestCommonAncestor.findLCA(LowestCommonAncestor.root, 4, 5).key, 2)
    
    def test_rightTree(self):
        self.assertEqual(LowestCommonAncestor.findLCA(LowestCommonAncestor.root, 6, 7).key, 3)

    def test_sameNode(self):
        self.assertEqual(LowestCommonAncestor.findLCA(LowestCommonAncestor.root, 1, 1).key, 1)

    def test_sameLine(self):
        self.assertEqual(LowestCommonAncestor.findLCA(LowestCommonAncestor.root, 2, 4).key, 2)




if __name__ == '__main__':
   unittest.main()
