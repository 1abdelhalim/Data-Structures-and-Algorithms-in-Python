def counting_sort(arr: list) -> list:
    length = len(arr)
    result = [0] * length  # output array
    k = max(arr)  
    count = [0] * (k + 1)  # to count occurrences
    
    # Counting occurrences of each element in the array
    for num in arr:
        count[num] += 1
    # 1 appears once in arr, 2 does not appear and so on 
    # [1, 0, 2, 2]
    

    # Calculating cumulative sum for element positions 
    for i in range(1, k + 1):
        count[i] += count[i - 1]
    # there is one number <= 1, one number <= 2 and so on 
    # [1, 1, 3, 5]
    

    # Placing elements in their correct positions in the output array
    for num in reversed(arr):
        result[count[num] - 1] = num
        count[num] -= 1

    return result
    # This is O(n+k) time complexity

    

# example 1 
print(counting_sort(arr=[4,1,3,4,3]))

# example 2
print(counting_sort(arr=[3,4,6,7,8,1,2,11,12]))