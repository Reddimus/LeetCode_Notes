import heapq

# Heap/Priority Queue approach
# T: O(E log V), M: O(V + E)
# Where E is the number of edges and V is the number of vertices

class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        # Build adjacency list based off bidirectional edges and weighted probabilities
        adj = [[] for node in range(n)]
        for idx, (a, b) in enumerate(edges):
            adj[a].append((succProb[idx], b))
            adj[b].append((succProb[idx], a))

        # Perform dijkstras algorithm to keep track of highest probability
        unvisited = None
        highest = [unvisited for node in range(n)]
        hq = [(-1, start_node)] # Max heap
        while hq and highest[end_node] == unvisited:
            p1, n1 = heapq.heappop(hq)
            if highest[n1] != unvisited:
                continue

            highest[n1] = p1

            for p2, n2 in adj[n1]:
                if highest[n2] == unvisited:
                    heapq.heappush(hq, (p1 * p2, n2))

        # If end node is reachable return end node's highest probability
        return -highest[end_node] if highest[end_node] != unvisited else 0