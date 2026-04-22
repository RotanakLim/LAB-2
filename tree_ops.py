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
        
#take input "BT" and return length of values in "BT"
def size(bt: BinaryTree) -> int:
    if bt is None:
        return 0
    return 1 + size(bt.left) + size(bt.right)

#take input "BT" and return leaf nodes 
def num_leaf_nodes(bt: BinaryTree) -> int:
    if bt is None:
        return 0
    if bt.left is None and bt.right is None:
        return 1
    return num_leaf_nodes(bt.left) + num_leaf_nodes(bt.right)

# return sum of values of input "BT"
def sum(bt: BinaryTree) -> int:
    if bt is None:
        return 0
    return bt.value + sum(bt.left) + sum(bt.right)

# return height or length from longest path from root to node of "BT"
def height(bt: BinaryTree) -> int:
    if bt is None:
        return 0
    return 1 + max(height(bt.left), height(bt.right))

# return "True" when node has a value "n" and child value of "3n"
def has_triple(bt: BinaryTree) -> bool:
    if bt is None:
        return False
    left_match = bt.left is not None and bt.left.value == 3 * bt.value
    right_match = bt.right is not None and bt.right.value == 3 * bt.value
    return left_match or right_match or has_triple(bt.left) or has_triple(bt.right)

# return Binarytree where each node value is smaller by one
def sub_one_map(bt: BinaryTree) -> BinaryTree:
    if bt is None:
        return None
    return BTNode(bt.value - 1,
                  sub_one_map(bt.left),
                  sub_one_map(bt.right))
        



class Tests(unittest.TestCase):
    def test_size(self) -> None:
        self.assertEqual(size(None), 0)
        self.assertEqual(size(BTNode(10, BTNode(5, None, None), BTNode(15, None, None))), 3)

    def test_num_leaf_nodes(self) -> None:
        self.assertEqual(num_leaf_nodes(None), 0)
        self.assertEqual(num_leaf_nodes(BTNode(1, BTNode(2, None, None), BTNode(3, None, None))), 2)

    def test_sum(self) -> None:
        self.assertEqual(sum(None), 0)
        self.assertEqual(sum(BTNode(1, BTNode(2, None, None), BTNode(3, None, None))), 6)

    def test_height(self) -> None:
        self.assertEqual(height(None), 0)
        self.assertEqual(height(BTNode(1, BTNode(2, BTNode(3, None, None), None), None)), 3)

    def test_has_triple(self) -> None:
        self.assertFalse(has_triple(BTNode(4, BTNode(5, None, None), None)))
        self.assertTrue(has_triple(BTNode(4, BTNode(12, None, None), None)))

    def test_sub_one_map(self) -> None:
        self.assertEqual(sub_one_map(None), None)
        self.assertEqual(
            sub_one_map(BTNode(3, BTNode(2, None, None), None)),
            BTNode(2, BTNode(1, None, None), None)
        )


    





# Remember from Lab 1: this if statements checks
# whether this module (ghg.py) is the module
# being executed or whether it's just being
# imported from some other module.
if (__name__ == '__main__'):    
    unittest.main()