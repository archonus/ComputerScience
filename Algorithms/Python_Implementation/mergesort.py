def top_down_merge(left_arr, right_arr):
    """
    A function to merge two *sorted* arrays together and return the result
    :param left_arr: The left_arr array
    :param right_arr: The right_arr array
    :return: A sorted array that contains all elements from both arrays
    """
    left_i = 0
    right_i = 0
    result = []
    while left_i < len(left_arr) and right_i < len(right_arr): #Compare all the elements
        if left_arr[left_i] <= right_arr[right_i]: #If the one on the left_arr is <= than right_arr, add the left_arr one first
            result.append(left_arr[left_i])
            left_i += 1
        else:
            result.append(right_arr[right_i])
            right_i += 1
    #Only one of the following while loops should run, depending on which array was larger
    while left_i < len(left_arr): #If left_arr had elements left_arr over
        result.append(left_arr[left_i])
        left_i += 1
    while right_i < len(right_arr): #If right_arr had elements left_arr over
        result.append(right_arr[right_i])
        right_i += 1
    return result

def top_down_merge_sort(arr):
    """
    Function to return a sorted array using merge sort
    :param arr: Input array to be sorted
    :return: A sorted array containing all the elements from arr
    """
    n = len(arr)
    if n > 1: #If the array is not a single element
        mid = n // 2 #The midpoint to split the array
        left_arr = top_down_merge_sort(arr[:mid]) #Sort the left half of the array
        right_arr = top_down_merge_sort(arr[mid:]) #Sort the right half of the array
        arr = top_down_merge(left_arr,right_arr) #Merge the two halves
    return arr

def bottom_up_merge_sort(numbers):
    """
    Bottom up approach to mergesort
    :param numbers: The list to be sorted
    """
    n = len(numbers)
    high = n - 1 #Last index
    current_size = 1
    while current_size < high:
        for l in range(0, n - 1, 2 * current_size):  # Iterate from 0 to n-1, with steps of 2*current_size
            mid = l + current_size - 1
            r = min((l + 2 * current_size - 1), high)
            bottom_up_merge(numbers, l, mid, r)
        current_size *= 2  # Double the size of the sub-array (1,2,4,8,16,...)
    return numbers


def bottom_up_merge(arr, start, mid, end):
    """Bottom up merging function"""
    n1 = mid - start + 1 #Size of the left array
    n2 = end - mid #The size of the right array
    left_arr = [0] * n1 #Initialise left_arr. It needs to be done like this to ensure that the main array is not affected
    right_arr = [0] * n2 #Initialise right_arr
    for i in range(0, n1): #Populate the left_arr
        left_arr[i] = arr[start + i]
    for i in range(0, n2): #Populate the right_arr
        right_arr[i] = arr[mid + i + 1]
    left_i = 0
    right_i = 0
    arr_i = start
    while left_i < len(left_arr) and right_i < len(right_arr):
        if left_arr[left_i] <= right_arr[right_i]:
            arr[arr_i] = left_arr[left_i]
            left_i += 1
        else:
            arr[arr_i] = right_arr[right_i]
            right_i += 1
        arr_i += 1
    while left_i < len(left_arr):
        arr[arr_i] = left_arr[left_i]
        arr_i += 1
        left_i += 1
    while right_i < len(right_arr):
        arr[arr_i] = right_arr[right_i]
        arr_i += 1
        right_i += 1
