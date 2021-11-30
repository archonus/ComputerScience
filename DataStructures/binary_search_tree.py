from __future__ import annotations
from typing import List, Tuple


class BinarySearchTree:

    class Node:
        def __init__(self, key, data, left: BinarySearchTree.Node = None, right: BinarySearchTree.Node = None):
            self.key = key
            self.data = data
            self.left = left
            self.right = right

    def __init__(self, data: List[Tuple] = None):
        self.root = None
        self._count = 0
        if data:
            for k, v in data:
                self.insert(k, v)
    
    def __len__(self):
        return self._count

    def insert(self, key, value):
        node = BinarySearchTree.Node(key, value)
        self._count += 1
        if self.root is None:
            self.root = node
            return
        current = None
        next = self.root

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
        current = self.root
        while current is not None:
            if key == current.key:
                return current.data
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        raise KeyError #The key was not in the BST


if __name__ == "__main__":
    pass
