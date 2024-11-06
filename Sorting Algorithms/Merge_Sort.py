# Merge Sort Using Iterative Method

def mergeSort(a1,a2,a3):
    m=len(a1)
    n=len(a2)
    p1=p2=p3=0
    while p1!=m and p2!=n:
        if a1[p1]<=a2[p2]:
            a3[p3]=a1[p1]
            p1+=1
        else:
            a3[p3]=a2[p2]
            p2+=1
        p3+=1
    if p1!=m:
        p2,n=p1,m
    # while p1!=m:
    #     a3[p3]=a1[p1]
    #     p1+=1
    #     p3+=1
    while p2!=n:
        a3[p3]=a2[p2]
        p2+=1
        p3+=1
a1=[1,2,3,5,7,9]
a2=[1,2,5,9,11,15,18]
a3=[0]*(len(a1)+len(a2))
mergeSort(a1,a2,a3)
print(a3)


# Merge Sort Using Recursion
def mergeSortRec(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        mergeSortRec(left_half)
        mergeSortRec(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1 
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original Array: ",arr)
result=mergeSortRec(arr)
print("Sorted Array: ",result)



# Time Complexity:

# Best Case: O(nlogn)
# Average Case: O(nlogn)
# Worst Case: O(nlogn)

# Space Complexity: O(n)