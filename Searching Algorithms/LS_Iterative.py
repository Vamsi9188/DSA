# Linear Search using Iterative Method

# Using for loop

def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
arr=[12,21,33,4,5]
x=4
result=linearSearch(arr,x)
if result!=-1:
    print(f"The target element {x} found at position {result}")
else:
    print("The target element not found")

# Using While Loop
def linearSearch(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i += 1
    return -1
arr = [3, 4, 9, 12, 21, 45]
target = 21
result = linearSearch(arr, target)
if result != -1:
    print(f"The Target element {target} found at index {result}")
else:
    print("The target element not found")


# Using do while loop
def linearSearch(arr, target):
    i = 0
    while True:
        if arr[i] == target:
            return i
        i += 1
        if i >= len(arr):
            return -1

arr = [3, 4, 9, 12, 21, 45]
target = 33
result = linearSearch(arr, target)
if result != -1:
    print(f"The Target element {target} found at index {result}")
else:
    print("The target element not found")