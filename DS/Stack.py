# 1. We can use python list as a stack.

# 2. Implementation using collections.deque
'''
Deque is preferred over list in cases where we need to quickly append and pop from both the ends.
Deque provides an O(1)time complexity for append and pop,
while list provides O(n)time complexity. The same methods (append() and pop()) are used on deque as on list.
'''
# 3. Implementation using queue module (LIFO queue)



# Array-based stack (python list يا معلم)
'''
Array-based approach is preferable when:

Random access to elements is required.
The size of the stack or queue is fixed or bounded.
Memory usage needs to be more efficient.
'''

class Stack:
    def __init__(self):
        # Create an empty list to be the storage for the stack
        self.stack = []

    def push(self, item):
        # Add the item to the top of stack
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            # Remove and return the top item from stack
            return self.stack.pop()
        else:
            raise IndexError("empty stack")
    def peek(self):
        if len(self.stack) > 0:
            # Return the top item from stack
            return self.stack[-1]
        else:
            raise IndexError("empty stack")
    def isEmpty(self):  
        # Return True if stack is empty
        return len(self.stack) == 0
    def size(self):
        # Return the number of items in stack
        return len(self.stack)
    

# Linked stack
'''
Linked list-based approach is preferable when:

Efficient insertion and deletion of elements are crucial.
Memory usage flexibility is important.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None  # Represents the top of the stack

    def push(self, item):
        new_node = Node(item)  # Create a new node with the given item
        new_node.next = self.top  # Set the next of the new node to the current top
        self.top = new_node  # Update the top to the new node

    def pop(self):
        if not self.is_empty():
            popped_item = self.top.data  # Store the data of the top node to be popped
            self.top = self.top.next  # Update the top to the next node
            return popped_item  # Return the popped item
        else:
            raise IndexError("Stack is empty")  # Raise an error if the stack is empty

    def peek(self):
        if not self.is_empty():
            return self.top.data  # Return the data of the top node without removing it
        else:
            raise IndexError("Stack is empty")  # Raise an error if the stack is empty

    def is_empty(self):
        return self.top is None  # Returns True if the stack is empty

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next  # Traverse the linked list and count the nodes
        return count  # Return the size of the stack


