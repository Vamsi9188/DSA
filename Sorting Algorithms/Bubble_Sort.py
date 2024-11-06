# Bubble Sort in Iterative Method

def bubbleSort(arr):
    n=len(arr)
    for iter_num in range(n-1): # n
        for i in range(n-1-iter_num): #n-1
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr
arr=[12,21,33,4,5,9]
print("Original Array: ",arr)
result=bubbleSort(arr)
print("Sorted Array: ",result)


# Using Recursion

def bubbleSortRec(arr,n=None):
    if n is None:
        n=len(arr)
    if n==1:
        return arr
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    return bubbleSort(arr)
arr=[3,9,2,6,4,5,8,1]
print("Original Array: ",arr)
result=bubbleSortRec(arr)
print("Sorted Array: ",result)


# Time Complexity:

# Best Case: O(n**2)
# Average Case: O(n**2)
# Worst Case: O(n**2)

# Space Complexity: O(1)


