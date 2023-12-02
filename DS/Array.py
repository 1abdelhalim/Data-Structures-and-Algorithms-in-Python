class DynamicArray:
    def __init__(self):
        self.length = 0  # Initialize the length of the dynamic array to 0
        self.data = {}  # Initialize an empty dictionary to store the array elements

    def get(self, index):
        return self.data[index]  # Retrieve the element at the specified index

    def push(self, item):
        self.data[self.length] = item  # Add the item to the dictionary at the current length index
        self.length += 1  # Increment the length by 1 after adding the item

        return self.length  # Return the updated length of the dynamic array

    def pop(self):
        if self.length == 0:
            return None  # Return None if the array is empty

        popped_item = self.data[self.length - 1]  # Get the last item from the dictionary
        self.data[self.length - 1] = None  # Set the last item to None to remove it
        self.length -= 1  # Decrement the length by 1 after removing the item

        return popped_item  # Return the removed item

    def insert(self, index, item):
        if index > self.length - 1 or index < 0:
            return None  # Return None if the index is out of bounds

        self.length += 1  # Increment the length by 1

        for i in range(self.length - 1, index - 1, -1):
            self.data[i] = self.data[i - 1]  # Shift the elements to the right to make space for the new item

        self.data[index] = item  # Insert the item at the specified index

        return self.data  # Return the updated dynamic array

    def remove(self, index):
        if self.length == 0:
            return None  # Return None if the array is empty

        if index > self.length - 1 or index < 0:
            return None  # Return None if the index is out of bounds

        item_to_be_removed = self.data[index]  # Get the item to be removed

        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]  # Shift the elements to the left to remove the item

        self.data[self.length - 1] = None  # Set the last element to None
        self.length -= 1  # Decrement the length by 1 after removing the item

        return item_to_be_removed  # Return the removed item
