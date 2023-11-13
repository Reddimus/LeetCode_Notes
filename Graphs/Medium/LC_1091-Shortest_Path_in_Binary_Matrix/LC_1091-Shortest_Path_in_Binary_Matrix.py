from collections import deque

# Matrix Graphs - Breadth First Search (BFS) approach
# T: O(n^2), M: O(n^2), where n is the number of rows and columns in the grid
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)   # n * n grid, n == rows == cols
        q = deque()     # queue cells w/ length
        # If starting cell & goal cell are not blocked
        if grid[0][0] == 0 and grid[n-1][n-1] == 0:
            grid[0][0] = 1       # visited cell
            q.append((0, 0, 1))  # First cell (row, col), length = 1
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                        (1, 1), (-1, -1), (1, -1), (-1, 1)]

        # While there is a valid path queued or goal not reached
        while q:
            curr_row, curr_col, curr_len = q.popleft()
            if curr_row == n-1 and curr_col == n-1:
                return curr_len
            
            # Explore if neighboring nodes are a valid path
            for dir_row, dir_col in directions:
                nghbr_row = curr_row + dir_row
                nghbr_col = curr_col + dir_col
                # if neighboring cell is not blocked & has not been visited
                if ((-1 < nghbr_row < n) and 
                (-1 < nghbr_col < n) and 
                grid[nghbr_row][nghbr_col] == 0):
                    grid[nghbr_row][nghbr_col] = 1  # visited cell
                    q.append((nghbr_row, nghbr_col, curr_len + 1))
            
        return -1

# Example 1:
attempt = Solution().shortestPathBinaryMatrix(grid=[[0,1], 
                                                    [1,0]])
assert attempt == 2, f"Expected 2, but got {attempt}"

# Example 2:
attempt = Solution().shortestPathBinaryMatrix(grid=[[0,0,0],
                                                    [1,1,0],
                                                    [1,1,0]])
assert attempt == 4, f"Expected 4, but got {attempt}"

# Example 3:
attempt = Solution().shortestPathBinaryMatrix(grid=[[1,0,0],
                                                    [1,1,0],
                                                    [1,1,0]])
assert attempt == -1, f"Expected -1, but got {attempt}"

# Test Case 4:
attempt = Solution().shortestPathBinaryMatrix(grid=[[0]])
assert attempt == 1, f"Expected 1, but got {attempt}"

# Test Case 5:
attempt = Solution().shortestPathBinaryMatrix(grid=[[1]])
assert attempt == -1, f"Expected -1, but got {attempt}"

# Test Case 6:
attempt = Solution().shortestPathBinaryMatrix(grid=[[0,0,0,0,0,0,1],
                                                    [1,1,1,1,1,0,1],
                                                    [1,0,0,1,1,0,0],
                                                    [0,1,1,0,1,0,1],
                                                    [0,1,1,1,0,0,1],
                                                    [0,1,1,1,1,1,1],
                                                    [0,0,0,0,0,0,0]])
assert attempt == 21, f"Expected 21, but got {attempt}"