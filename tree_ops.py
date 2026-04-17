from typing import *
from dataclasses import dataclass
import unittest
import math
import sys
sys.setrecursionlimit(10**6)

BinaryTree : TypeAlias = Union[ 'BTNode', None ]
@dataclass(frozen=True)
class BTNode:
    value : Any
    left : BinaryTree
    right : BinaryTree

# helper function to avoid repeptive code
def empty_tree(BT:BinaryTree):
        if BT.value is None:
            return 0 
        
#take input "BT" and return length of values in "BT"
def size (BT: BinaryTree) -> int:
    empty_tree() 
    return 1 + BT.left + BT.right

#take input "BT" and return leaf nodes 
def num_leaf_nodes(BT: BinaryTree):
    empty_tree()
    if BT.left is None and BT.right is None:
        return 1
    else:
        return BT.left + BT.right

# return sum of values of input "BT"
def sum(BT: BinaryTree) -> int:
    empty_tree()
    total = BT.value + BT.left + BT.right
    return total

# return height or length from longest path from root to node of "BT"
def height(BT:BinaryTree):
    empty_tree()
    return 1 + max(BT.left) + max(BT.right)

# return "True" when node has a value "n" and child value of "3n"
def has_triple(BT: BinaryTree):
        empty_tree()
        left_match  = BT.left  != 0 and BT.left.value  == 3 * BT.value
        right_match = BT.right != 0 and BT.right.value == 3 * BT.value
        return left_match or right_match

# return Binarytree where each node value is smaller by one
def sub_one_map(BT: BinaryTree):
        empty_tree()
        return BTNode(
            BT.value - 1,
            (BT.left),
            BT.right)
        



class Tests(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(BTNode(5)), 5)
        self.assertEqual(sum(BTNode(5), BTNode(2)), 7)
    def test_size(self):
        self.assertEqual(size(BTNode(0)), 0)
        self.assertEqual(size(BTNode(5), BTNode(2), BTNode(4) ), 12)
    def test_num_leaf_nodes(self):
        self.assertEqual(num_leaf_nodes(BTNode(10), 1))
        self.assertEqual(num_leaf_nodes(BTNode(10), BTNode(5), BTNode(7)), 12)
    def test_height(self):
        self.assertEqual(height(BTNode(5), BTNode(1)), 1)
        self.assertEqual(height(BTNode(5), BTNode(3), BTNode(4), BTNode(2), BTNode(3)))
    def test_has_triple(self):
        self.assertEqual(has_triple(BTNode(2), BTNode(0), BTNode(3)), 6)
        self.assertEqual(has_triple(BTNode(0), BTNode(0), BTNode(3)), 0)
    def test_sub_one_map(self):
        self.assertEqual(sub_one_map((BTNode(5), BTNode(1))), BTNode(4), BTNode(0))
        self.assertEqual(sub_one_map(BTNode(0)), 0)


    





# Remember from Lab 1: this if statements checks
# whether this module (ghg.py) is the module
# being executed or whether it's just being
# imported from some other module.
    if (__name__ == '__main__'):    
        unittest.main()