from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List, Tuple
from dictionary import Dictionary

@dataclass
class Node:
    """A node in a binary search tree"""
    key : Any
    data : Any
    left : Node | None = None
    right : Node | None = None

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

    def _inorder(self, current_node : Node, node_ls : List[Node]) -> None:
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

    def minimum(self) -> Node:
        current = self._root
        while current.left is not None:
            current = current.left
        return current

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

    def _replace_child(self, parent : Node, is_left_child : bool, new_child : Node):
        if parent is None: # Trying to replace root
            self._root = new_child
        else:
            if is_left_child:
                parent.left = new_child
            else:
                parent.right = new_child

    def delete(self, key):
        parent = None
        is_left_child = False # Which child of the parent is it
        current = self._root
        while current is not None: # Find the node
            if current.key == key:
                break # Found node
            parent = current
            if key < current.key:
                is_left_child = True
                current = current.left
            else:
                is_left_child = False
                current = current.right

        if current is None:
            raise KeyError # Key not in tree

        # There are two cases. The simpler case is where there are no children or only one child. The complex case is when there are two children

        if current.left is None: # No left node, so replace node with right node (which may be itself null)
            self._replace_child(parent, is_left_child, current.right)

        elif current.right is None: # No right node, so replace node with left node (which is not null since it's an elif)
            self._replace_child(parent, is_left_child, current.left)

        else: # There are two children. We use the successor to delete. Could also use the predecessor
            successor = current.right
            successor_parent = current
            if successor.left is not None: # Find the successor in the right subtree
                while successor.left is not None:
                    successor_parent = successor
                    successor = successor.left

                self._replace_child(successor_parent, is_left_child=False, new_child=successor.right) # Replace the successor node with its right child
            successor.left = current.left # Replace left subtree of successor (which necessarily did not have a left child)
            self._replace_child(parent, is_left_child, successor)


    def inorder_traverse(self) -> List[Node]:
        node_list = []
        self._inorder(self._root,node_list)
        return node_list

    @property
    def keys(self):
        return [node.key for node in self.inorder_traverse()]


if __name__ == "__main__":
    bst = BinarySearchTree([(14,"first"),(11,"second"),(23,"third"),(5,"fourth"),(12,"fifth")])
    bst.update(5,"changed fourth")
    print(bst[5])
    print(bst.minimum())
    print(bst.inorder_traverse())
    bst.delete(11)
    print(bst.keys)
