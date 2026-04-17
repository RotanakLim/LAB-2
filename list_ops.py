from typing import *
from dataclasses import dataclass
import unittest
import math
import sys
sys.setrecursionlimit(10**6)


@dataclass(frozen=True)
class LLNode:
    value: int
    rest: LinkedList

LinkedList: TypeAlias = Union[None, LLNode]

#Takes an int_list and returns the number of nodes in that list
def length(int_list: LinkedList) -> int:
    if int_list is None:
        return 0
    return 1 + length(int_list.rest)

#Takes a linked list(int_list) and returns the sum of all values in the list
def sum(int_list: LinkedList) -> int:
    if int_list is None:
        return 0
    return int_list.value + sum(int_list.rest)

#count_greater_than counts how many values in int_list are greater than the threshold
def count_greater_than(int_list: LinkedList, threshold: int) -> int:
    if int_list is None:
        return 0
    if int_list.value > threshold:
        return 1 + count_greater_than(int_list.rest, threshold)
    else:
        return count_greater_than(int_list.rest, threshold)

#find returns the index of value in int_list, or None if it's not found
def find(int_list: LinkedList, value: int):
    return find_helper(int_list, value, 0)

def find_helper(int_list: LinkedList, value: int, index: int):
    if int_list is None:
        return None
    if int_list.value == value:
        return index
    return find_helper(int_list.rest, value, index + 1)

#returns a new linked list where each value in int_list is decrease by 1
def sub_one_map(int_list: LinkedList):
    if int_list is None:
        return None
    return LLNode(int_list.value - 1, sub_one_map(int_list.rest))

#returns a new sorted list with value added to int_list
def insert(int_list: LinkedList, value: int):
    if int_list is None:
        return LLNode(value, None)
    if value <= int_list.value:
        return LLNode(value, int_list)
    return LLNode(int_list.value, insert(int_list.rest, value))

class Tests(unittest.TestCase):

    def test_length(self):
        self.assertEqual(length(None), 0)

        lst = LLNode(1, LLNode(2, LLNode(3, None)))
        self.assertEqual(length(lst), 3)

    def test_sum(self):
        self.assertEqual(sum(None), 0)

        lst = LLNode(1, LLNode(2, LLNode(3, None)))
        self.assertEqual(sum(lst), 6)

    def test_count_greater_than(self):
        self.assertEqual(count_greater_than(None, 10), 0)

        lst = LLNode(3, LLNode(12, LLNode(7, LLNode(20, None))))
        self.assertEqual(count_greater_than(lst, 10), 2)

    def test_find(self):
        self.assertEqual(find(None, 5), None)

        lst = LLNode(3, LLNode(7, LLNode(2, None)))
        self.assertEqual(find(lst, 7), 1)

    def test_sub_one_map(self):
        self.assertEqual(sub_one_map(None), None)

        self.assertEqual(
            sub_one_map(LLNode(5, LLNode(3, LLNode(1, None)))),
            LLNode(4, LLNode(2, LLNode(0, None)))
        )

    def test_insert(self):
        self.assertEqual(insert(None, 5), LLNode(5, None))

        self.assertEqual(
            insert(LLNode(2, LLNode(4, LLNode(6, None))), 5),
            LLNode(2, LLNode(4, LLNode(5, LLNode(6, None))))
        )
# Remember from Lab 1: this if statements checks
# whether this module (ghg.py) is the module
# being executed or whether it's just being
# imported from some other module
if (__name__ == '__main__'):
 unittest.main()

