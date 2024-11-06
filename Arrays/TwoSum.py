# Find the indexes in which their elements sum equal to target

def twoSum(arr,target):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return [i,j]
arr=[2,7,11,15]
target=9
result=twoSum(arr,target)
print(f"The element {target} is the sum found by adding {arr} indices are: {result}")


# Using Hashing
def twoSum(nums,target):
    n=len(nums)
    m={}
    for i in range(n):
        cur=nums[i]
        if target-cur in m:
            return [m[target-cur],i]
        m[cur]=i
nums=[3,2,4]
target=6
result=twoSum(nums,target)
print(f"The element {target} is the sum found by adding {nums} indices are: {result}")


# Time Complexity: O(n**n)
