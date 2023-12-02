def selection_sort(arr):
    sorted_arr = []
    while arr:
        smallest_index = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[smallest_index]:
                smallest_index = i
        sorted_arr.append(arr.pop(smallest_index))
    return sorted_arr

print(selection_sort([5, 3, 6, 2, 10]))
