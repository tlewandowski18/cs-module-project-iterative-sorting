def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    start = 0
    end = len(arr) - 1
    while end >= start:
        #get middle point
        middle_index = (start + end) // 2
        #if the middle value is same as target, set found to Trun
        if arr[middle_index] == target:
            return middle_index
        #move start or end index closer to the other, shrinking search space
        else:
            if target < arr[middle_index]:
                end = middle_index - 1
            if target > arr[middle_index]:
                start = middle_index + 1
    return -1
