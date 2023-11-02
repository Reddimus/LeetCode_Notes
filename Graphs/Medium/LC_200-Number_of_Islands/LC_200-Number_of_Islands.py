import collections

# T & M: O(m * n), where m = rows and n = cols from grid input
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])
        self.visited = set()

        count = 0
        for r in range(self.rows):
            for c in range(self.cols):
                # if land and coordinates not visited
                if grid[r][c] == "1" and (r, c) not in self.visited:
                    self.dfs(r, c)
                    # self.bfs(r, c)
                    count += 1
        return count

    def dfs(self, r: int, c: int) -> None:
        if (
            r < 0 or self.rows <= r or
            c < 0 or self.cols <= c or
            self.grid[r][c] == "0" or
            (r, c) in self.visited 
        ):
            return  # water reached or coordinates already visited
        
        self.visited.add((r, c))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dir_r, dir_c in directions:
            self.dfs(r + dir_r, c + dir_c)  # go deeper into path

    def bfs(self, r: int, c: int) -> None:
        self.visited.add((r, c))
        q = collections.deque() # visit coordinates in FCFS/FIFO order
        q.append((r, c))

        # while there are connected land coordinates to visit
        while q:
            curr_r, curr_c = q.popleft()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dir_r, dir_c in directions:
                neighb_r, neighb_c = curr_r + dir_r, curr_c + dir_c
                # if neigboring coordinates are land & not visited
                if (
                    -1 < neighb_r < self.rows and
                    -1 < neighb_c < self.cols and
                    self.grid[neighb_r][neighb_c] == "1" and
                    (neighb_r, neighb_c) not in self.visited
                ):
                    q.append((neighb_r, neighb_c))
                    self.visited.add((neighb_r, neighb_c))
    
sol = Solution()

# Example 1:
attempt = sol.numIslands(grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
])
assert attempt == 1, f'Expected 1, but got {attempt}'

# Example 2:
attempt = sol.numIslands(grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
])
assert attempt == 3, f'Expected 3, but got {attempt}'

# Test Case 3:
attempt = sol.numIslands(grid = [
    ["0","0","1","0","0","1","0","0","0","0","0","0","0","0","1","1","0","1","0","0"],
    ["0","1","0","0","0","0","1","1","0","0","0","1","0","0","1","1","0","0","0","0"],
    ["1","0","1","1","0","0","0","0","0","1","0","0","0","1","0","1","1","1","1","0"],
    ["1","1","0","0","0","0","0","0","0","0","1","0","0","1","1","1","1","1","1","1"],
    ["0","0","0","0","0","1","0","0","0","1","1","1","1","0","1","0","0","0","0","0"],
    ["0","1","1","1","0","0","0","1","0","1","0","1","0","0","1","0","1","1","0","0"],
    ["0","0","0","0","0","0","0","0","1","1","1","0","0","1","1","0","0","0","0","0"],
    ["0","1","1","0","0","0","0","0","1","0","1","1","0","1","1","0","0","1","0","0"],
    ["0","0","1","1","1","0","0","1","0","0","0","0","0","0","0","1","1","1","0","1"],
    ["1","1","0","0","0","1","0","1","0","0","0","1","1","0","0","1","0","1","1","0"],
    ["0","0","0","0","0","0","1","0","1","1","0","0","1","0","1","1","1","1","0","1"],
    ["0","0","1","1","0","0","1","0","1","0","0","1","0","0","1","0","0","1","0","1"],
    ["0","1","0","0","0","0","0","1","0","0","0","0","0","0","1","1","1","0","0","0"],
    ["0","0","1","0","1","0","0","1","1","0","1","1","1","0","0","1","1","0","0","1"],
    ["1","0","1","0","1","0","1","0","0","0","0","0","0","0","1","0","0","1","1","0"],
    ["1","0","1","1","1","0","1","0","0","0","0","0","0","1","0","0","0","0","1","1"],
    ["1","0","0","0","0","1","0","0","0","0","0","0","1","0","0","0","0","0","1","1"],
    ["0","0","0","0","0","0","1","0","0","0","1","0","1","0","1","1","0","1","0","1"],
    ["1","0","0","1","0","0","0","0","0","0","1","0","0","0","0","0","1","1","1","1"],
    ["0","0","0","1","1","0","0","0","0","0","0","0","0","1","0","0","0","1","0","0"]
])
assert attempt == 45, f'Expected 45, but got {attempt}'