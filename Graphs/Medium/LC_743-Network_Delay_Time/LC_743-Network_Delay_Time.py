import heapq

# Adjacency list Graphs - Dijkstra's algorithm approach
# T: O(E log V) = O(E log N), M: O(V + E) = O(N + E)
# Where E is the number of edges and V/N is the number of vertices/nodes

class Solution:
    def networkDelayTime(self, times: list[int], n: int, k: int) -> int:
        # Create adjacency list based on sorce node -> weight & target node
        adj = [[] for node in range(n + 1)]
        for ui, vi, wi in times:
            adj[ui].append((wi, vi))
        
        # Perform dijkstras algorithm to keep track of time passed
        time = 0
        unvisited = n + 2
        shortest = [unvisited for node in range(n + 1)]
        pq = [(time, k)]
        while pq:
            w1, n1 = heapq.heappop(pq)
            # If the node's shortest path has already been mapped
            if shortest[n1] != unvisited:
                continue
            shortest[n1] = w1
            time = w1
            n -= 1  # Keep track of number of nodes visited

            for w2, n2 in adj[n1]:
                if shortest[n2] == unvisited:
                    heapq.heappush(pq, (w1 + w2, n2))
        # If all nodes are reachable return the tracked time
        return time if n <= 0 else -1

# Example 1:
attempt = Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)
answer = 2
assert attempt == answer, f"Expected {answer}, but got {attempt}"
# Example 2:
attempt = Solution().networkDelayTime(times = [[1,2,1]], n = 2, k = 1)
answer = 1
assert attempt == answer, f"Expected {answer}, but got {attempt}"
# Example 3:
attempt = Solution().networkDelayTime(times = [[1,2,1]], n = 2, k = 2)
answer = -1
assert attempt == answer, f"Expected {answer}, but got {attempt}"
# Test Case 4:
attempt = Solution().networkDelayTime(times = [[1,2,1],[2,3,2],[1,3,2]], n = 3, k = 1)
answer = 2
assert attempt == answer, f"Expected {answer}, but got {attempt}"
# Test Case 5:
attempt = Solution().networkDelayTime(times = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]], n = 4, k = 1)
answer = -1
assert attempt == answer, f"Expected {answer}, but got {attempt}"
# Test Case 6:
attempt = Solution().networkDelayTime(times = [[1,5,66],[3,5,55],[4,3,29],[1,2,9],[3,4,10],[3,1,3],[2,3,78],[1,4,98],[4,5,21],[5,2,19],[5,1,76],[4,1,65],[3,2,27],[5,3,23],[5,4,12],[2,1,36],[4,2,75],[2,4,11],[1,3,30],[2,5,8]], n = 5, k = 1)
answer = 30
assert attempt == answer, f"Expected {answer}, but got {attempt}"
# Test Case 7:
attempt = Solution().networkDelayTime(times = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]], n = 3, k = 1)
answer = 4
assert attempt == answer, f"Expected {answer}, but got {attempt}"