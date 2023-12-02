class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Check if the linked list is empty.
        Returns:
            bool: True if the linked list is empty, False otherwise.
        """
        return self.head is None

    def insert_at_end(self, data):
        """
        Insert a new node with the given data at the end of the linked list.
        Args:
            data: The data value to be inserted.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_beginning(self, data):
        """
        Insert a new node with the given data at the beginning of the linked list.
        Args:
            data: The data value to be inserted.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete_at_end(self):
        """
        Delete the node at the end of the linked list.
        """
        if self.is_empty():
            print("Linked list is empty")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None

    def delete_at_beginning(self):
        """
        Delete the node at the beginning of the linked list.
        """
        if self.is_empty():
            print("Linked list is empty")
        else:
            self.head = self.head.next

    def delete_at_position(self, position):
        """
        Delete the node at the specified position in the linked list.
        Args:
            position (int): The position of the node to be deleted.
        """
        if self.is_empty():
            print("Linked list is empty")
        elif position == 1:
            self.delete_at_beginning()
        else:
            current = self.head
            count = 1
            while current and count < position - 1:
                current = current.next
                count += 1
            if current and current.next:
                current.next = current.next.next

    def display(self):
        """
        Display the contents of the linked list.
        """
        if self.is_empty():
            print("Linked list is empty")
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()

    def search(self, data):
        """
        Search for a node with the given data in the linked list.
        Args:
            data: The data value to search for.
        Returns:
            bool: True if the data is found, False otherwise.
        """
        if self.is_empty():
            print("Linked list is empty")
            return False
        else:
            current = self.head
            while current:
                if current.data == data:
                    return True
                current = current.next
            return False

    def reverse(self):
        """
        Reverse the linked list.
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Creating a linked list and performing operations
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_beginning(55)
ll.insert_at_end(100)
ll.insert_at_end(23)
ll.insert_at_end(56)
ll.insert_at_beginning(13)

ll.display()  # Output: 13 55 10 20 30 100 23 56

print(ll.search(20))  # Output: True
print(ll.search(15))  # Output: False

ll.delete_at_end()
ll.delete_at_beginning()

ll.display()  # Output: 55 10 20 30 100 23 
