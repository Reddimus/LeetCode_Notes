# Graphs - Disjoint Set Union (DSU) approach
# T: O(N * α(N)) ≈ O(N), M: O(N)
# Where N is the number of nodes and α is the Inverse Ackermann function which is roughly O(1) time complexity.

class DisjointSetUnion:
    # Initialize nodes to single sized node graphs
    def __init__(self, n: int) -> None:
        self.parent = [*(range(n))]
        self.size = [1] * n

    # Recursively find and assign parent of current node
    def findParent(self, v: int) -> int:
        if self.parent[v] == v:
            return v
        # Path compression optimization
        self.parent[v] = self.findParent(self.parent[v])
        return self.parent[v]
    
    # Attempt to union two components
    def unionComponents(self, a: int, b: int) -> bool:
        a, b = self.findParent(a), self.findParent(b)
        if a == b:	# If nodes are already in same component
            return False

        if self.size[a] < self.size[b]:
            a, b = b, a	# Union by size optimization
        # Merge smaller component (b) into larger component (a)
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        dsu = DisjointSetUnion(len(edges) + 1)
        for node_a, node_b in edges:
            # If node a part of the same component as node b
            if not dsu.unionComponents(node_a, node_b):
                return [node_a, node_b] # redundant connection
        return []

# Example 1
attempt = Solution().findRedundantConnection(edges = [[1,2],[1,3],[2,3]])
answer = [2, 3]
assert attempt == answer, f"Expected {answer}, but got {attempt}"
# Example 2
attempt = Solution().findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]])
answer = [1, 4]
assert attempt == answer, f"Expected {answer}, but got {attempt}"
