import heapq

# Dijkstra's algorithm approach
# T: O(N^2 * log N), M: O(N^2)
# Where N is size of each side of the 2-D grid

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        goal = (n - 1, n - 1)

        shortest = {}
        hq = [(grid[0][0], 0, 0)]   # Minimum heap
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Perform dijkstras algorithm to keep track of time passed
        while hq and goal not in shortest:
            t1, r1, c1 = heapq.heappop(hq)
            # If the coordinate's shortest path has already been mapped
            if (r1, c1) in shortest:
                continue
            
            shortest[(r1, c1)] = t1 # Map current time

            # Check all neighboring coordinates
            for dr, dc in directions:
                r2, c2 = r1 + dr, c1 + dc
                if (0 <= r2 <= n - 1 and
                0 <= c2 <= n - 1 and
                (r2, c2) not in shortest):
                    # New time is the maximum time of current path
                    heapq.heappush(hq, (max(t1, grid[r2][c2]), r2, c2))

        # Return the time it takes to reach the goal
        return shortest[goal]