def insertion_sort(arr):
    n = len(arr)
    
    # Traverse through 1 to n-1
    for i in range(1, n):
        key = arr[i]
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("Sorted array:", arr)
