# # Find Two Missing Numbers | Set 2 (XOR based solution)

# Input  : arr[] = {1, 3, 5, 6}, n = 6
# Output : 2 4

# Input : arr[] = {1, 2, 4}, n = 5
# Output : 3 5

# Input : arr[] = {1, 2}, n = 4
# Output : 3 4

def findMissingTwoNumbers(n,arr):
    x=arr[0]
    for i in range(1,n-2):
        x=x^arr[i]
    for i in range(1,n+1):
        x=x^i
    j=x & ~(x-1)
    x=0
    y=0
    for i in range(0,n-2):
        if arr[i] & j:
            x=x^arr[i]
        else:
            y=y^arr[i]
    for i in range(1,n+1):
        if i & j:
            x=x^i
        else:
            y=y^i
    return [x,y]
n=6
arr=[1,3,5,6]
result=findMissingTwoNumbers(n,arr)
print("The missing two numbers are:",result)