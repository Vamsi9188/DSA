# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex source to vertex destination.

# Given edges and the integers n, source, and destination, return 1 if there is a valid path from source to destination, or 0 otherwise.

# Input Format:
# First Parameter: Number of vertex n
# Second Parameter: matrix edges of size mat_dims[0] x mat_dims[1]
# Third parameter: number source
# Fourth Parameter: number destination

# Output Format:
# Return the number.

# Example 1:
# "1"

# Input: 
# 3
# 3 2
# 0 1
# 1 2
# 2 0
# 0
# 2
# Output:
# 1
# Explanation: 3 2 represents the size of the matrix. 
# There are two paths from vertex 0 to vertex 2:
#      -0->1->2
#      -0->2

# Example 2:
# "1"
# Input: 
# 6
# 5 2
# 0 1
# 0 2
# 3 5
# 5 4
# 4 3
# 0
# 5
# Output:
# 0
# Explanation: 5 2 represents the size of the matrix.
# There is no path from vertex 0 to vertex 5.

# Constraints:
# 1 <= n <= 2 * 105
# 0 <= edges.length <= 2 * 105
# edges[i].length == 2
# 0 <= ui, vi <= n - 1
# ui != vi
# 0 <= source, destination <= n - 1
# There are no duplicate edges.
# There are no self edges.
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)
# 12


from collections import deque, defaultdict
def solve(n, edges, source, destination):
    if source == destination:
        return 1    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * n
    queue = deque([source])
    visited[source] = True
    while queue:
        node = queue.popleft()
        if node == destination:
            return 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return 0

n=3
edges=[[3,2],[0,1],[1,2],[2,0]]
source=0
destination=2
result=solve(n,edges,source,destination)
print("The Output for this Question is:",result)