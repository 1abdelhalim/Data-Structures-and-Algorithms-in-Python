def quicksort(arr):
    # Base case: If the array has less than 2 elements, it is already sorted
    if len(arr) < 2:
        return arr
    else:
        # Choose the pivot element using the median of three strategy
        first = arr[0]
        middle = arr[len(arr)//2]
        last = arr[-1]
        pivot = sorted([first, middle, last])[1]

        # Partition the array into two sub-arrays:
        # - Elements less than the pivot
        # - Elements greater than or equal to the pivot
        less = [x for x in arr if x < pivot]
        greater_or_equal = [x for x in arr if x >= pivot]

        # Recursively sort the sub-arrays and combine the results
        return quicksort(less) + quicksort(greater_or_equal)


arr = [8, 2, 4, 7, 1, 3, 9, 6, 5]
sorted_arr = quicksort(arr)
print(sorted_arr)
