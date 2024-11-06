# Tim Sort is a hybrid sorting algorithm derived from mergeSort sort and insertion sort. It is used as the default sorting algorithm in Python (since version 2.3), and in Java's `Arrays.sort()` for objects. Tim Sort is designed to perform well on many kinds of real-world data, and it has the following key characteristics:

# Stable: Maintains the relative order of equal elements.
# Adaptive: Takes advantage of existing order in the data.

# Tim Sort Using Iterative Method:

def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def mergeSort(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left = arr[l:l + len1]
    right = arr[m + 1:m + 1 + len2]

    i = j = 0
    k = l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right[j]
        j += 1
        k += 1

def timSort(arr):
    n = len(arr)
    min_run = 32

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertionSort(arr, start, end)

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                mergeSort(arr, left, mid, right)
        size *= 2

    return arr
arr=[12,21,33,4,5,9]
print("Original Array: ",arr)
result=timSort(arr)
print("Sorted Array: ",result)


# Tim Sort Using Recursion Method
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def mergeSort(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left = arr[l:l + len1]
    right = arr[m + 1:m + 1 + len2]

    i = j = 0
    k = l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right[j]
        j += 1
        k += 1

def timSortRec(arr, start, end):
    if start >= end:
        return

    min_run = 32

    if end - start < min_run:
        insertionSort(arr, start, end)
        return

    mid = (start + end) // 2

    timSortRec(arr, start, mid)
    timSortRec(arr, mid + 1, end)

    mergeSort(arr, start, mid, end)

# Wrapper function
def timSort(arr):
    timSortRec(arr, 0, len(arr) - 1)
    return arr
arr=[5,2,37,1,9,12,0,9]
print("Original Array: ",arr)
result=timSort(arr)
print("Sorted Array: ",result)

# Time Complexity:

# Best Case: O(nlogn)
# Average Case: O(nlogn)
# Worst Case: O(nlogn)

# Space Complexity: O(n)