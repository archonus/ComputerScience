from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from dictionary import Dictionary

@dataclass
class HashTableItem:
    """Class representing an item in the hash table"""
    key : Any
    value : Any
    next : HashTableItem = None

class HashTable(Dictionary):
    """Hash table implementation using separate chaining"""
    INITIAL_CAPACITY = 8  # The intitial capacity of the hash table. Should implement resizing

    def __init__(self, initial_data=None):
        # The list is initialised to all None
        self._buckets : list[HashTableItem] = [None for i in range(HashTable.INITIAL_CAPACITY)]
        self._count = 0
        if(initial_data):
            for key, value in initial_data:
                self.insert(key, value)

    def __len__(self):
        return self._count

    def __repr__(self) -> str:
        return repr(self._buckets) #Simply for debugging purposes

    def _get_index(self, key):
        # Hash the key and find the index
        return hash(key) % self.capacity
    
    def _find_item(self, key) -> HashTableItem:
        """Find the HashTableItem from the key. Raises KeyError if cannot find"""
        index = self._get_index(key)
        if self._buckets[index] is None:  # If the bucket is empty
            raise KeyError
        current_item = self._buckets[index]
        while current_item.key != key:
            if current_item.next is None:  # There are no more items to check and key has not been found
                raise KeyError
            else:  # Move to next item in linked list
                current_item = current_item.next
        return current_item

    @property
    def capacity(self):
        return len(self._buckets)

    @property
    def load_factor(self):
        return self._count / self.capacity

    def insert(self, key, value):
        """Insert an item into the hash table"""
        item = HashTableItem(key, value)
        index = self._get_index(key)
        if(self._buckets[index] is None):  # The bucket is empty
            self._buckets[index] = item
        else:  # Collision
            # Store a reference to the current item in the bucket
            item.next = self._buckets[index]
            # Replace the contents of the bucket with the current item. This creates a linked list
            self._buckets[index] = item
        self._count += 1  # Increment the value of count

    def retrieve(self, key):
        """Retrieve the value from the key. Raises KeyError if key not found"""
        item = self._find_item(key)
        return item.value

    def update(self, key, value):
        """Update the value of an item in the table from its key. Raises KeyError if key not found"""
        item = self._find_item(key)
        item.value = value

    def delete(self, key):
        """Delete an item from the hash table from its key. Raises KeyError if key not found"""
        index = self._get_index(key)
        if self._buckets[index] is None:  # If the bucket is empty
            raise KeyError
        current_item = self._buckets[index]
        if current_item.key == key: #Head of the linked list
            self._buckets[index] = current_item.next #Move the pointer along, or to None if there is not another item
            del current_item
            self._count -= 1
        else: #Not the head of the list, so need the previous node as well as the next
            prev = self._buckets[index]
            current_item = prev.next
            while current_item is not None:
                if current_item.key == key:
                    prev.next = current_item.next
                    del current_item
                    self._count -= 1
                    return
                prev = current_item
                current_item = current_item.next
            raise KeyError #While loop finished without finding the key



if __name__ == "__main__":
    ht = HashTable()
    ht.insert(9, "bucket 1 first")
    ht[1] = "bucket 1 second"
    ht[2] = "bucket 2 first"
    print(ht.retrieve(9))
    print(ht[1])
    print(ht)
    ht.delete(1)
    print(ht)
