class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        check if the doubly linked list is empty.
        returns:
            bool: True if the doubly linked list is empty, False otherwise.
        """
        return self.head is None

    def insert_at_end(self, data):
        """
        Insert a new node with the given data at the end of the doubly linked list.
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
            new_node.prev = current

    def insert_at_beginning(self, data):
        """
        Insert a new node with the given data at the beginning of the doubly linked list.
        Args:
            data: The data value to be inserted.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_at_end(self):
        """
        Delete the node at the end of the doubly linked list.
        """
        if self.is_empty():
            print("Doubly linked list is empty")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None

    def delete_at_beginning(self):
        """
        Delete the node at the beginning of the doubly linked list.
        """
        if self.is_empty():
            print("Doubly linked list is empty")
        else:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    def delete_at_position(self, position):
        """
        Delete the node at the specified position in the doubly linked list.
        Args:
            position (int): The position of the node to be deleted.
        """
        if self.is_empty():
            print("Doubly linked list is empty")
        elif position <= 0:
            print("Invalid position")
        elif position == 1:
            self.delete_at_beginning()
        else:
            current = self.head
            count = 1
            while current and count < position:
                current = current.next
                count += 1
            if current:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev

    def display_forward(self):
        """
        Display the contents of the doubly linked list in forward order.
        """
        if self.is_empty():
            print("Doubly linked list is empty")
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()

    def display_backward(self):
        """
        Display the contents of the doubly linked list in backward order.
        """
        if self.is_empty():
            print("Doubly linked list is empty")
        else:
            current = self.head
            while current.next:
                current = current.next
            while current:
                print(current.data, end=" ")
                current = current.prev
            print()


# Creating a doubly linked list and performing operations
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_beginning(15)
dll.insert_at_beginning(55)
dll.insert_at_beginning(35)
dll.insert_at_beginning(65)

dll.display_forward()  # Output: 65 35 55 15 10 20 30 
dll.display_backward()  # Output: 30 20 10 15 55 35 65

dll.delete_at_end()
dll.delete_at_beginning()

dll.display_forward()  # Output: 35 55 15 10 20
dll.display_backward()  # Output: 20 10 15 55 35
