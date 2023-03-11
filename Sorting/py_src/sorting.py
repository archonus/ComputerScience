#Vaibhav Mahajan - Sorting Algorithms

def insertion_sort(nums):
    for j in range(1, len(nums)): #Iterate through the array n-1 times
        next_num = nums[j] #Store the value of the next number to i
        i = j - 1 #Set i to the index before j
        while i >= 0 and nums[i] > next_num: #Move the element to the correct place
            nums[i + 1] = nums[i]
            i -= 1
        nums[i + 1] = next_num #Move next_num to the place where the while loop stopped
    return nums

def bubble_sort(arr):
    n = len(arr) #Start at the end
    while n >= 1: #Keep going to the end
        for i in range(n-1): #Inner loop for each element, excluding the last n terms 
            temp = arr[i] #The element being looked
            if temp > arr[i + 1]: #If the element is larger than the one next to it, it should be swapped
                #Swap them
                arr[i] = arr[i+1]
                arr[i+1] = temp
        n -= 1
    return arr

def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i #The placeholder for the index of the minimum
        for j in range(i + 1, n): #Go from the index i onwards to find the minimum
            if nums[min_idx] > nums[j]: #If a new minimum is found
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]


if __name__ == "__main__":
    a = [3,56,78,34,12,0,89,23]
    selection_sort(a)
    print(a)
