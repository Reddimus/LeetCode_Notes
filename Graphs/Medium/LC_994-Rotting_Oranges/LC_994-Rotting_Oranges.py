from collections import deque
# Matrix Graphs - Breadth First Search (BFS) approach
# T & M: O(m*n), where m == rows and n = columns
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        rotten_cells = deque()  # queue indices of rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotten_cells.append((r, c))
        
        minutes = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # While there are fresh oranges and rotten oranges queued
        while fresh > 0 and rotten_cells:
            # Rotten all neighboring oranges at the same time
            for same_minute in range(len(rotten_cells)):
                curr_row, curr_col = rotten_cells.popleft()
                for dir_row, dir_col in directions:
                    nghbr_row = dir_row + curr_row
                    nghbr_col = dir_col + curr_col
                    if ((-1 < nghbr_row < rows) and
                    (-1 < nghbr_col < cols) and
                    grid[nghbr_row][nghbr_col] == 1):
                        grid[nghbr_row][nghbr_col] = 2
                        rotten_cells.append((nghbr_row, nghbr_col))
                        fresh -= 1

            minutes += 1
        
        if fresh == 0:
            return minutes
        return -1

# Example 1:
attempt = Solution().orangesRotting(grid=[[2,1,1],
                                          [1,1,0],
                                          [0,1,1]])
assert attempt == 4, f"Expected 4, but got {attempt}"

# Example 2:
attempt = Solution().orangesRotting(grid=[[2,1,1],
                                          [0,1,1],
                                          [1,0,1]])
assert attempt == -1, f"Expected -1, but got {attempt}"

# Example 3:
attempt = Solution().orangesRotting(grid=[[0,2]])
assert attempt == 0, f"Expected 0, but got {attempt}"

# Test Case 4:
attempt = Solution().orangesRotting(grid=[[0]])
assert attempt == 0, f"Expected 0, but got {attempt}"

# Test Case 5:
attempt = Solution().orangesRotting(grid=[[1]])
assert attempt == -1, f"Expected -1, but got {attempt}"

# Test Case 6:
attempt = Solution().orangesRotting(grid=[[2]])
assert attempt == 0, f"Expected 0, but got {attempt}"
