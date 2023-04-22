from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class DisjointSetNode:
    k: Any
    parent: DisjointSetNode = None
    rank: int = 1

    @property
    def is_root(self):
        return self.parent is None


class DisjointSet:

    def __init__(self, *ks) -> None:
        self._nodes = {k: DisjointSetNode(k) for k in ks}

    def add(self, k):
        # Adds a new set consisting of a single item k
        if k in self._nodes:
            raise ValueError('Key already in a set')
        self._nodes[k] = DisjointSetNode(k)

    def find_set(self, node: DisjointSetNode):
        if node.is_root:
            return node
        else:
            # Traverse up and perform path compression
            node.parent = self.find_set(node.parent)
            return node.parent

    def __getitem__(self, k) -> DisjointSetNode:
        # Returns a handle to the set containing item k
        node = self._nodes[k]
        return self.find_set(node)

    def merge(self, h: DisjointSetNode, i: DisjointSetNode):
        # Merge set-with-handle h and set-with-handle i
        if h.rank > i.rank:
            i.parent = h
        elif h.rank == i.rank:
            i.parent = h
            h.rank += 1  # Increment rank since they have same rank
        else:
            h.parent = i

    def iter_from(self, k):
        # Returns all items in the subset containing k
        handle = self[k]
        for key, node in self._nodes.items():
            if self.find_set(node) == handle:
                yield key


if __name__ == '__main__':
    s = DisjointSet(1, 2, 3, 4)
