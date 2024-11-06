# Selection Sort Using Iterative Method

def selectionSort(arr):
    n=len(arr)
    for iter_num in range(n):
        min_idx=iter_num
        for i in range(iter_num+1,n):
            if arr[min_idx]>arr[i]:
                min_idx=i
        arr[min_idx],arr[iter_num]=arr[iter_num],arr[min_idx]
    return arr
arr=[9,2,5,4,1,7,3,8,6]
print("Sorted Array: ",arr)
result=selectionSort(arr)
print("Sorted Array: ",result)


# Selection Sort using Recursion Method

def selectionSortRecursive(arr, start=0):
    if start >= len(arr) - 1:
        return arr
    min_idx = start
    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    arr[start], arr[min_idx] = arr[min_idx], arr[start]
    return selectionSortRecursive(arr, start + 1)
arr = [9, 2, 5, 4, 1, 7, 3, 8, 6]
print("Original Array:", arr)
result = selectionSortRecursive(arr)
print("Sorted Array:", result)

# Time Complexity:

# Best Case: O(n**2)
# Average Case: O(n**2)
# Worst Case: O(n**2)

# Space Complexity: O(1)