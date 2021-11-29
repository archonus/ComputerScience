def _partition(arr, low, high):
    """
    Function to partition an array
    :param arr: The main array from which to get the elements
    :param low: The start of the sub-array being looked at
    :param high: The end of the sub-array being looked at
    :return: The index of the pivot element
    """
    i = low - 1 #Set to this because it is incremented by one later
    pivot = arr[high] #Choose the pivot element to be the highest array.
    for j in range(low,high): #Go through the entire array
        if arr[j] <= pivot: #If the element is less than or equal to the pivot element
            i += 1
            arr[i], arr[j] = arr[j], arr[i] #Swap the ith element with the jth element
    arr[i+1], arr[high] = arr[high], arr[i + 1] #The point i+1 is the point where all the elements are
    return i + 1 #The index of the pivot element

def quick_sort(arr, low, high):
    """
    The main quicksort function
    :param arr: The array to be sorted
    :param low: The start of the sub-array to be sorted. To sort the entire array, set to 0
    :param high: The end of the sub-array to be sorted. To sort the entire array, set to len(a) - 1
    """
    if len(arr) == 1: #If the length is 1, the array is already sorted
        return arr
    if low < high: #As long as low and high are not the same and are in the right order, sort the sub-array
        p_i = _partition(arr,low,high) #The partition function will return the index of the pivot element
        quick_sort(arr,low, p_i - 1) #Sort the left half of the partitioned sub-array recursively
        quick_sort(arr,p_i + 1, high) #Sort the right half of the partitioned array recursively
    return arr
