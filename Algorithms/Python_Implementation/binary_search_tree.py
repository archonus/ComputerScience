from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List, Tuple
from dictionary import Dictionary

@dataclass
class Node:
    """A node in a binary search tree"""
    key : Any
    data : Any
    left : Node = None
    right : Node = None

class BinarySearchTree(Dictionary):
    """Class representing a binary search tree"""

    def __init__(self, data: List[Tuple] = None):
        self._root = None
        self._count = 0
        if data: # Insert data if it exists
            for k, v in data:
                self.insert(k, v)
    
    def __len__(self):
        return self._count

    def insert(self, key, value):
        node = Node(key, value)
        self._count += 1
        if self._root is None:
            self._root = node
            return
        current = None
        next = self._root

        while next is not None:  # Next is none => The space has been found
            current = next
            if key == current.key:  # Overwrite instead of inserting
                current.data = value
                return

            if key < current.key:
                next = current.left
            else:
                next = current.right

        if key < current.key:
            current.left = node
        else:
            current.right = node
    
    def retrieve(self,key):
        return self._find_item(key).data #Return the data of the item

    def update(self, key, data):
        node = self._find_item(key)
        node.data = data

    def inorder_traverse(self):
        node_list = []
        self._inorder(self._root,node_list)
        return node_list
    
    def _inorder(self, current_node : Node, node_ls : List):
        if current_node is None:
            return
        self._inorder(current_node.left, node_ls)
        node_ls.append(current_node)
        self._inorder(current_node.right, node_ls)

    def _find_item(self, key):
        current = self._root
        while current is not None:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        raise KeyError #The key was not in the BST


    @property
    def keys(self):
        return [node.key for node in self.inorder_traverse()]


if __name__ == "__main__":
    bst = BinarySearchTree([(14,"first"),(1,"second"),(23,"third"),(5,"fourth"),(11,"fifth")])
    bst.update(5,"changed fourth")
    print(bst[5])
    print(bst.keys)
