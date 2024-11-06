# Linear Search Using Recursive Method

# Using For loop

def linearSearch(arr, index, key):
    if index == -1:
        return -1
    if arr[index] == key:
        return index
    return linearSearch(arr, index-1, key)
arr=[12,21,33,4,5,9,45]
index=1
key=21
result=linearSearch(arr,index,key)
if result!=-1:
    print(f"The target element {key} found at index {result}");
else:
    print("The target element not found")


# Using While loop
def linearSearch(arr, target, i=0):
    while i < len(arr):
        if arr[i] == target:
            return i
        i += 1
        if i < len(arr):
            return linearSearch(arr, target, i)
    return -1

arr = [3, 4, 9, 12, 21, 45]
target = 21
result = linearSearch(arr, target)
if result != -1:
    print(f"The Target element {target} found at index {result}")
else:
    print("The target element not found")




# Using do while loop
def linearSearch(arr, target, i=0):
    while True:
        if arr[i] == target:
            return i
        i += 1
        if i >= len(arr):
            return -1
        if i < len(arr):
            return linearSearch(arr, target, i)

arr = [3, 4, 9, 12, 21, 45]
target = 45
result = linearSearch(arr, target)
if result != -1:
    print(f"The Target element {target} found at index {result}")
else:
    print("The target element not found")
