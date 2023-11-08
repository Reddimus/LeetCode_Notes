import collections

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                # if land and coordinates not visited
                if (grid[r][c] == 1):
                    max_area = max(max_area, self.bfs(r, c, rows, cols, grid))
        return max_area
    
    def bfs(self, r: int, c: int, rows: int, cols: int, grid: list[list[int]]) -> int:
        grid[r][c] = 0  # visited cell
        q = collections.deque() # visit coordinates in FCFS/FIFO order
        q.append((r, c))

        area = 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # while there are connected land coordinates to visit
        while q:
            curr_r, curr_c = q.popleft()
            for dir_r, dir_c in directions:
                neighb_r, neighb_c = curr_r + dir_r, curr_c + dir_c
                # if neigboring coordinates are land & not visited
                if (
                (-1 < neighb_r < rows) and
                (-1 < neighb_c < cols) and
                grid[neighb_r][neighb_c] == 1
                ):
                    grid[neighb_r][neighb_c] = 0    # visited cell
                    q.append((neighb_r, neighb_c))
                    area += 1
        
        return area # return's island's area
        




# Example 1
attempt = Solution().maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                                            [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                            [0,1,1,0,1,0,0,0,0,0,0,0,0],
                                            [0,1,0,0,1,1,0,0,1,0,1,0,0],
                                            [0,1,0,0,1,1,0,0,1,1,1,0,0],
                                            [0,0,0,0,0,0,0,0,0,0,1,0,0],
                                            [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                            [0,0,0,0,0,0,0,1,1,0,0,0,0]])
assert attempt == 6, f'Expected 6, but got {attempt}'

# Example 2
attempt = Solution().maxAreaOfIsland(grid = [[0,0,0,0,0,0,0,0]])
assert attempt == 0, f'Expected 0, gut got {attempt}'

# Test Case 3
attempt = Solution().maxAreaOfIsland(grid=[[0]])

# Test Case 4
attempt = Solution().maxAreaOfIsland(grid=[[1]])