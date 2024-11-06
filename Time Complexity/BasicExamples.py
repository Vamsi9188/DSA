#1 Single Statements
# Assignment Operations: O(1)

x=5          #O(1)
y=5          #O(1)
print(x+y)   #O(1)
# Time Complexity: O(1)+O(1)+O(1)=O(3)=O(1)

#2 Variable Declarations and Initializations
# Single Variable Declaration: O(1)
# List/Dictionary/Set Initialization: O(n) where n is the number of elements

a = 10  # O(1)
lst = [1, 2, 3]  # O(3) = O(n)

# 3. If Conditions
# Simple If Condition: O(1)
# Example:

if x > 0:   # O(1)
    y = 1

# 4. Nested If Conditions
# Multiple Nested If Conditions: The time complexity is still O(1) because it's evaluated once.

if x > 0:    # O(1)
    if y > 0:  # O(1)
        z = 1

# 5. Loops
# For Loop Traversing a List: O(n) where n is the length of the list
# While Loop: Depends on the number of iterations

n=10
for i in range(n):  # O(n)
    print(i)

while x > 0:   # O(n), depending on how x is reduced
    x -= 1

# 6. Nested Loops
# Nested For Loop: O(n^2) where n is the number of iterations of the inner and outer loop

n=5
for i in range(n):  # O(n)
    for j in range(n):  # O(n)
        print(i, j)  # Total = O(n * n) = O(n^2)

# 7. List Operations
# Indexing: O(1)
# Appending an element: O(1)
# Inserting an element at an index: O(n)
# Removing an element: O(n)
# Sorting: O(n log n)

lst[2]  # O(1)
lst.append(5)  # O(1)
lst.insert(2, 10)  # O(n)
lst.sort()  # O(n log n)

# 8. Function Calls
# Function Call Overhead: O(1) (but the body of the function will determine the overall complexity)

def simple_function():  # O(1)
    return 1
simple_function()  # O(1)

# 9. Recursion
# Simple Recursion: Time complexity depends on the number of recursive calls.
# Tree Recursion: If a function makes two recursive calls, the time complexity is O(2^n).

def factorial(n):  # O(n)
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):  # O(2^n)
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 10. String Operations
# Concatenation: O(k) where k is the length of the final string
# Indexing: O(1)

s = "Hello" + "World"  # O(len("HelloWorld")) = O(k)
s[0]  # O(1)

# 11. Dictionary Operations
# Insertion/Update: O(1)
# Lookup: O(1)
# Deletion: O(1)

# 12. Set Operations


# Insertion/Deletion: O(1)
# Checking Membership: O(1)

s = set()  # O(1)
s.add(1)  # O(1)
s.remove(1)  # O(1)
if 1 in s:  # O(1)
    print("Found")


# 13. Comprehensive Examples

# Finding the Maximum Element in a List
max_value = max(lst)  # O(n)

# Sum of All Elements in a List
total = sum(lst)  # O(n)

# Binary Search in a Sorted List
def binary_search(arr, x):  # O(log n)
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Matrix Multiplication (2D Arrays)
A=[[1,2],[2,3]]
B=[[1,2],[2,3]]
result=[]
for i in range(n):          # O(n)
    for j in range(n):      # O(n)
        for k in range(n):  # O(n)
            result[i][j] += A[i][k] * B[k][j]

# Total = O(n^3)

# Depth-First Search (DFS) in a Graph
def dfs(graph, start, visited=None):  # O(V + E)
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

# Breadth-First Search (BFS) in a Graph
def bfs(graph, start):  # O(V + E)
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


# Key Takeaways
# O(1): Constant time operations.
# O(log n): Operations that divide the problem space in half each time (e.g., binary search).
# O(n): Linear time operations that require a single pass through the data.
# O(n^2): Quadratic time operations (e.g., nested loops).
# O(2^n): Exponential time, often found in recursive problems.
