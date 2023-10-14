class Solution:
    # Bottom-Up Approach
    # T: O(m*n), M: O(n), where m is num of rows, n is num of cols
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [0] * n  # Solve last row base case

        for row in range(m-1, -1, -1):
            curr_row = [0] * n
            curr_row[n - 1] = 1 # Solve last col base case

            # Solve curr case using bottom up approach
            for col in range(n-2, -1, -1):
                curr_row[col] = curr_row[col + 1] + prev_row[col]
            
            prev_row = curr_row
        
        return prev_row[0]

    '''
    # 2-D Dynamic Programming - Full Grid/Bottom-Up Approach
    # T&M: O(m*n), where m is num of rows, n is num of cols
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for ln in range(m)]

        # Solve base case for last row & last cols
        for row in range(m):
            grid[row][n-1] = 1
        for col in range(n):
            grid[m-1][col] = 1
        print(grid)

        # Solve for the rest of the grid using bottom-up approach
        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                grid[row][col] = grid[row+1][col] + grid[row][col+1]
        print(grid)

        return grid[0][0]
    '''

sol = Solution()

# Ex1:
attempt = sol.uniquePaths(m = 3, n = 7)
assert attempt == 28, f'Expected {28}, but got {attempt}'
# Ex2:
attempt = sol.uniquePaths(m = 3, n = 2)
assert attempt == 3, f'Expected {3}, but got {attempt}'
