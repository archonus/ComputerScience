class FibHeapNode:
    def __init__(self, id, priority) -> None:
        self.priority = priority
        self.id = id

        self.parent: FibHeapNode = None
        self.child: FibHeapNode = None

        # Doubly-linked circular queue
        self.left: FibHeapNode = self
        self.right: FibHeapNode = self

        self.degree = 0
        self.marked = False

    def __repr__(self) -> str:
        return f"FibHeapNode(id = {self.id}, priority = {self.priority}, degree={self.degree})"

    @property
    def is_root(self):
        return self.parent is None

    def add_sibling(self, node):
        """Add in a node as a sibling, updating the parent as well"""

        node.left = self
        node.right = self.right
        node.parent = self.parent

        self.right.left = node
        self.right = node

        if self.parent:  # Not in the root list
            self.parent.degree += 1

    def add_child(self, node):
        """Splice in a node into the children list"""

        node.parent = self

        if self.degree == 0:  # First child
            self.child = node

        else:
            node.left = self.child
            node.right = self.child.right

            self.child.right.left = node
            self.child.right = node

        self.degree += 1

    def remove_from_siblings(self):
        """Splice out of the siblings list and update parent"""

        if self.is_root:  # No parent to update
            self.left.right = self.right
            self.right.left = self.left

            # Reset the left and right pointers
            self.left = self
            self.right = self

        else:
            if self.parent.degree == 1:  # Only child of parent
                self.parent.child = None
            else:
                # Update siblings
                self.left.right = self.right
                self.right.left = self.left

                if self.parent.child == self:
                    # Change the child pointer of the parent to an arbitrary sibling
                    self.parent.child = self.right

                # Reset the left and right pointers
                self.left = self
                self.right = self

            self.parent.degree -= 1

        self.parent = None  # Reset parent
        return self


class FibHeap:

    def __init__(self) -> None:
        self.min_node: FibHeapNode = None
        self._nodes = {}

    def push(self, x, priority):
        # push a new item x into the heap
        if x in self._nodes:
            raise ValueError(f"Item {x} already exists")

        node = FibHeapNode(x, priority)

        self._nodes[x] = node

        if self.min_node:
            self.min_node.add_sibling(node)

            if priority < self.min_node.priority:  # Update min node if necessary
                self.min_node = node
        else:
            self.min_node = node

    def _decreasekey_node(self, node: FibHeapNode, new_priority):
        if new_priority > node.priority:
            raise ValueError("New priority must be smaller")
        elif new_priority == node.priority:
            # Do nothing where the priority does not change
            return

        node.priority = new_priority  # Change priority

        if node.is_root:  # In the root list
            if node.priority < self.min_node.priority:
                self.min_node = node

        elif node.parent.priority > node.priority:
            # Min heap violation can only occur if not in root list

            parent = node.parent

            # Min heap violation, so put into root list
            node.remove_from_siblings()
            node.marked = False
            self.min_node.add_sibling(node)

            if self.min_node.priority > node.priority:
                self.min_node = node

            # Loser enforcement
            while not parent.is_root and parent.marked:  # Parent also moved into root list
                grandparent = parent.parent
                # Put parent into root list
                parent.remove_from_siblings()
                parent.marked = False
                self.min_node.add_sibling(parent)

                # Look at parent's parent
                parent = grandparent

            if not parent.is_root:  # Loop terminated because there was an unmarked parent
                parent.marked = True

    def decreasekey(self, x, priority):
        # decrease the priority for item x
        node = self._nodes[x]
        self._decreasekey_node(node, priority)

    def _get_roots(self) -> set[FibHeapNode]:
        start_id = self.min_node.id
        roots = [self.min_node]
        current = self.min_node.right

        while current.id != start_id:
            roots.append(current)
            current = current.right

        return roots

    def _cleanup(self):
        roots = self._get_roots()

        root_array = {}
        for node in roots:
            node.remove_from_siblings()
            x = node  # The root of the tree, which could change when linking the two trees
            d = x.degree
            while d in root_array:
                # Ensures that there is only one tree of each degree
                y: FibHeapNode = root_array[d]
                if x.priority < y.priority:
                    y.remove_from_siblings()  # Remove from root list
                    x.add_child(y)
                    
                else:
                    x.remove_from_siblings()
                    y.add_child(x)
                    x = y  # Update for next iteration
                del root_array[d]  # The entry in d has been subsumed
                y.marked = x.marked = False # Update loser flag
                d += 1  # Adding a child has increased the degree
            root_array[d] = x
        #print(root_array)

        self.min_node = None
        for root_node in root_array.values(): # Re-insert into root list
            if self.min_node is None:
                self.min_node = root_node
            else:
                self.min_node.add_sibling(root_node)
                if self.min_node.priority > root_node.priority:
                    self.min_node = root_node

    def popmin(self):
        # Returns an item whose priority is minimal in the heap

        if len(self._nodes) == 0:
            raise ValueError("Queue is empty")

        prev_min = self.min_node

        del self._nodes[prev_min.id]  # Remove from list of nodes


        if len(self._nodes) != 0:
            # There are still items in the queue
            while prev_min.child:  # The children need to be put into root list
                node = prev_min.child
                node.remove_from_siblings()  # Remove the child
                self.min_node.add_sibling(node)  # Add to root list

            self.min_node = prev_min.right

            assert self.min_node != prev_min

            prev_min.remove_from_siblings()
            self._cleanup()

        else:  # Queue is empty
            self.min_node = None

        return prev_min.id

    def __contains__(self, x):
        # returns True if the heap contains item x, False otherwise
        return x in self._nodes

    def __len__(self):
        return len(self._nodes)

    def __bool__(self):
        # returns True if the heap has any items at all, False otherwise
        return len(self) != 0


if __name__ == '__main__':
    import random
    
    fibheap = FibHeap()
    n = 64
    ls = list(range(n))
    random.seed(1)
    random.shuffle(ls)

    for i in range(n):
        fibheap.push(chr(65+i),ls[i])
    
    for i in range(n-5):
        print(fibheap.popmin())

    fibheap.decreasekey('S',1)
    fibheap.decreasekey('G',0)
    
    print(fibheap.min_node)

