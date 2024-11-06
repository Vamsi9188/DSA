# Insertion Sort using Iterative Method

def insertionSort(arr):
    n=len(arr)
    for wall in range(1,n):
        key=arr[wall]
        i=wall-1
        while i!=-1 and arr[i]>key:
            arr[i+1]=arr[i]
            i-=1
            arr[i+1]=key
    return arr
arr=[6,2,3,5,9,1,7,4,8]
print("Original Array: ",arr)
result=insertionSort(arr)
print("Sorted Array: ",result)

# Time Complexity:
# Best Case: O(n)
# Worst Case: O(n**2)
# Average Case: O(n**2)

# Space Complexity: O(1)



# Insertion Sort Using Recursion

def insertionSortRec(arr,n):
    if n<=1:
        return arr
    insertionSortRec(arr,n-1)
    key=arr[n-1]
    i=n-2
    while i>=0 and arr[i]>key:
        arr[i+1]=arr[i]
        i-=1
    arr[i+1]=key
    return arr
arr = [6, 2, 3, 5, 9, 1, 7, 4, 8]
print("Original Array:", arr)
result = insertionSortRec(arr, len(arr))
print("Sorted Array:", result)

# Time Complexity:

# Best Case: O(n)
# Average Case: O(n^2)
# Worst Case: O(n^2)

# Space Complexity:
# O(n)