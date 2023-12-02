# We can import queue.Queue or collections.deque 

#Array based (we have python list here)
'''
Array-based approach is preferable when:

Random access to elements is required.
The size of the stack or queue is fixed or bounded.
Memory usage needs to be more efficient.
'''

class Queue:
    def __init__(self):
        self.queue = []  # Initialize an empty list to store the queue elements

    def is_empty(self):
        return len(self.queue) == 0  # Returns True if the queue is empty

    def enqueue(self, item):
        self.queue.append(item)  # Add the item to the end of the queue

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # Remove and return the item from the front of the queue
        else:
            raise IndexError("Queue is empty")  # Raise an error if the queue is empty

    def size(self):
        return len(self.queue)  # Return the number of elements in the queue




# Linked Queue
'''
Linked list-based approach is preferable when:


Efficient insertion and deletion of elements are crucial.
Memory usage flexibility is important.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None  # Points to the head of the linked list
        self.tail = None  # Points to the tail of the linked list

    def is_empty(self):
        return self.head is None  # Returns True if the queue is empty

    def enqueue(self, item):
        new_node = Node(item)  # Create a new node with the given item
        if self.is_empty():
            # If the queue is empty, set both the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # If the queue is not empty, append the new node to the tail and update the tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")  # Raise an error if the queue is empty
        else:
            removed_item = self.head.data  # Store the data of the head node to be removed
            self.head = self.head.next  # Update the head to the next node
            if self.head is None:
                # If the head becomes None (no more nodes), update the tail to None as well
                self.tail = None
            return removed_item  # Return the removed item

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next  # Traverse the linked list and count the nodes
        return count  # Return the size of the queue

