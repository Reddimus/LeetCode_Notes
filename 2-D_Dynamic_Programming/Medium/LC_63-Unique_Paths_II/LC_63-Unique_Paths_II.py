def printArr(arr):
    for row in arr:
        print(row)

class Solution:
    # Bottom-Up Approach
    # T: O(m*n), M: O(n), where m = rows, n = cols
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * cols
        dp[-1] = 1  # goal base case

        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if obstacleGrid[r][c]:  # if obstacle
                    dp[c] = 0               # reset steps to 0
                elif c + 1 < cols:
                    dp[c] += dp[c+1]        # add steps from right
        
        return dp[0]
    
    '''
    # Bottom-Up approach with full dp grid
    # T: O(m*n), M: O(m*n), where m = rows, n = cols
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # print('Input grid:')
        # printArr(obstacleGrid)

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (cols+1) for row in range(rows+1)]
        dp[rows-1][cols-1] = 1  # goal base case

        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if obstacleGrid[r][c]:  # if obstacle
                    dp[r][c] = 0            # reset steps to 0
                else:
                    dp[r][c] += dp[r+1][c] + dp[r][c+1]
        
        # print('Final dp grid:')
        # printArr(dp)
        # print()

        return dp[0][0]
    '''

    '''
    # Top-Down Approach
    # T: O(m*n), M: O(n), where m = rows, n = cols
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * cols
        dp[0] = 1

        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c - 1 >= 0:
                    dp[c] += dp[c-1]

        return dp[-1]
    '''

    '''
    # Top-Down Approach with full dp grid
    # T: O(m*n), M: O(m*n), where m = rows, n = cols
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # print('Input grid:')
        # printArr(obstacleGrid)

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (cols+1) for row in range(rows+1)]
        dp[1][1] = 1

        for r in range(1, rows+1):
            for c in range(1, cols+1):
                if obstacleGrid[r-1][c-1]:
                    dp[r][c] = 0
                else:
                    dp[r][c] += dp[r-1][c] + dp[r][c-1]
        
        # print('Final dp grid:')
        # printArr(dp)
        # print()

        return dp[-1][-1]
    '''


sol = Solution()

# Ex1:
attempt = sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
assert attempt == 2, f'Expected 2 but got, {attempt}'
# Ex2:
attempt = sol.uniquePathsWithObstacles([[0,1],[0,0]])
assert attempt == 1, f'Expected 1 but got, {attempt}'
# Test Case 3:
attempt = sol.uniquePathsWithObstacles([[0,0],[1,1],[0,0]])
assert attempt == 0, f'Expected 0 but got, {attempt}'
# Test Case 4:
attempt = sol.uniquePathsWithObstacles([[0,0,0,0],[0,1,0,0],[0,0,0,0], [0,0,0,0]])
assert attempt == 8, f'Expected 7 but got, {attempt}'
# Test Case 5:
attempt = sol.uniquePathsWithObstacles([[0,1]])
assert attempt == 0, f'Expected 0 but got, {attempt}'
