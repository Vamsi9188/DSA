# Quick Sort using Iterative method

def quickSort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left = [x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quickSort(left)+middle+quickSort(right)
arr=[12,21,33,4,5,9]
print("Original Array: ",arr)
result=quickSort(arr)
print("Sorted Array: ",result)


# Quick Sort Using Recursion

def quickSortRec(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSortRec(arr, low, pi - 1)
        quickSortRec(arr, pi + 1, high)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
arr=[12,21,33,4,5,9]
print("Original Array: ",arr)
result=quickSort(arr)
print("Sorted Array: ",result)




# Time Complexity:

# Best Case: O(nlogn)
# Average Case: O(nlogn)
# Worst Case: O(n**2)

# Space Complexity: O(n)