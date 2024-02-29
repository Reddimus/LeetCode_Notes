# Graphs - Disjoint Set Union (DSU) approach
# T: O((n + m) * α(n)) ≈ O(n + m), M: O(n)
# Where N = # of nodes, M = # of edges, α(n) = Inverse Ackermann function

class DisjointSetUnion:
    # Initialize nodes to single sized node graphs
    def __init__(self, n: int) -> None:
        self.parents = [*range(n)]
        self.sizes = [1] * n
    
    # Recursively find and assign parent of current node
    def findParent(self, v: int) -> int:
        if self.parents[v] == v:
            return v
        # Path compression optimization
        return self.findParent(self.parents[v])
    
    # Attempt to union two components
    def unionComponents(self, a: int, b: int) -> bool:
        a, b = self.findParent(a), self.findParent(b)
        if a == b:  # If nodes are already in same component
            return False
        
        if self.sizes[a] < self.sizes[b]:
            a, b = b, a # Union by size optimization
        # Merge smaller component (b) into larger component (a)
        self.parents[b] = a
        self.sizes[a] += self.sizes[b]
        return True
    
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        # Union connected nodes
        dsu = DisjointSetUnion(n)
        for a, b in edges:
            dsu.unionComponents(a, b)
        
        return len(set(dsu.findParent(node) for node in range(n)))

# Example 1:
attempt = Solution().countComponents(n = 5, edges = [[0,1],[1,2],[3,4]])
answer = 2
assert attempt == answer, f"Expected {answer}, but got {attempt}"
# Example 2:
attempt = Solution().countComponents(n = 5, edges = [[0,1],[1,2],[2,3],[3,4]])
answer = 1
assert attempt == answer, f"Expected {answer}, but got {attempt}"