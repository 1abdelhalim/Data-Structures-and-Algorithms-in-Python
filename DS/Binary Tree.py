class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)



    def search(self, data):
        return self._search_recursive(self.root, data)

    

    def print_tree(self):
        self._print_tree_recursive(self.root)

    

# Example usage:
tree = BinaryTree()

tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

tree.print_tree()  # Output: 2 3 4 5 6 7 8

result = tree.search(6)
if result:
    print("\nFound")
else:
    print("\nNot found")
