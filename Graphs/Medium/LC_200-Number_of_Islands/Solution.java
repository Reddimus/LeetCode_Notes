import java.util.*;

// T & M: O(m * n), where m = rows and n = cols from grid input
class Solution {
    public int numIslands(char[][] grid) {
        int rows = grid.length, cols = grid[0].length;

        int count = 0;
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                // If the current cell is land & not visited
                if (grid[r][c] == '1') {
                    dfs(r, c, rows, cols, grid);
                    //bfs(r, c, rows, cols, grid);
                    ++count;
                }
            }
        }
        return count;
    }

    private void dfs(int r, int c, int rows, int cols, char[][] grid) {
        // If the current cell is out of bounds or water
        if (r < 0 || rows <= r ||
        c < 0 || cols <= c ||
        grid[r][c] != '1')
            return;

        grid[r][c] = 'V';   // cell visited

        dfs(r + 1, c, rows, cols, grid);    // down
        dfs(r - 1, c, rows, cols, grid);    // up
        dfs(r, c + 1, rows, cols, grid);    // right
        dfs(r, c - 1, rows, cols, grid);    // left
    }

    /*
    private static class Indicies {
        final int row, col;
        Indicies(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
    private void bfs(int r, int c, int rows, int cols, char[][] grid) {
        Queue<Indicies> q = new LinkedList<>();
        q.add(new Indicies(r, c));
        grid[r][c] = 'V';   // cell visited

        // while there are connected land cells to visit
        while(!q.isEmpty()) {
            Indicies currCell = q.poll();   // visit cells in FCFS/FIFO order
            Indicies[] directions = {new Indicies(1, 0), 
                                    new Indicies(-1, 0), 
                                    new Indicies(0, 1), 
                                    new Indicies(0, -1)};
            for (Indicies dir : directions) {
                int neighbRow = currCell.row + dir.row;
                int neighbCol = currCell.col + dir.col;
                // if neigboring cells are land & not visited
                if ((-1 < neighbRow && neighbRow < rows) &&
                (-1 < neighbCol && neighbCol < cols) &&
                grid[neighbRow][neighbCol] == '1') {
                    q.add(new Indicies(neighbRow, neighbCol));
                    grid[neighbRow][neighbCol] = 'V';
                }
            }
        }
    }
    */
}

class TestCases {
    public static void main(String[] args) {
        // In terminal:
        // Compile:     "javac Solution.java"
        // Test cases:  "java -ea TestCases"
        char[][] grid;
        int attempt;

        // Example 1:
        grid = new char[][] {
            {'1','1','1','1','0'},
            {'1','1','0','1','0'},
            {'1','1','0','0','0'},
            {'0','0','0','0','0'}
        };
        attempt = new Solution().numIslands(grid);
        assert attempt == 1 : "Expected 1, but got " + attempt;

        // Example 2:
        grid = new char[][] {
            {'1','1','0','0','0'},
            {'1','1','0','0','0'},
            {'0','0','1','0','0'},
            {'0','0','0','1','1'}
        };
        attempt = new Solution().numIslands(grid);
        assert attempt == 3 : "Expected 3, but got " + attempt;

        // Test case 3:
        grid = new char[][] {
            {'0','0','1','0','0','1','0','0','0','0','0','0','0','0','1','1','0','1','0','0'},
            {'0','1','0','0','0','0','1','1','0','0','0','1','0','0','1','1','0','0','0','0'},
            {'1','0','1','1','0','0','0','0','0','1','0','0','0','1','0','1','1','1','1','0'},
            {'1','1','0','0','0','0','0','0','0','0','1','0','0','1','1','1','1','1','1','1'},
            {'0','0','0','0','0','1','0','0','0','1','1','1','1','0','1','0','0','0','0','0'},
            {'0','1','1','1','0','0','0','1','0','1','0','1','0','0','1','0','1','1','0','0'},
            {'0','0','0','0','0','0','0','0','1','1','1','0','0','1','1','0','0','0','0','0'},
            {'0','1','1','0','0','0','0','0','1','0','1','1','0','1','1','0','0','1','0','0'},
            {'0','0','1','1','1','0','0','1','0','0','0','0','0','0','0','1','1','1','0','1'},
            {'1','1','0','0','0','1','0','1','0','0','0','1','1','0','0','1','0','1','1','0'},
            {'0','0','0','0','0','0','1','0','1','1','0','0','1','0','1','1','1','1','0','1'},
            {'0','0','1','1','0','0','1','0','1','0','0','1','0','0','1','0','0','1','0','1'},
            {'0','1','0','0','0','0','0','1','0','0','0','0','0','0','1','1','1','0','0','0'},
            {'0','0','1','0','1','0','0','1','1','0','1','1','1','0','0','1','1','0','0','1'},
            {'1','0','1','0','1','0','1','0','0','0','0','0','0','0','1','0','0','1','1','0'},
            {'1','0','1','1','1','0','1','0','0','0','0','0','0','1','0','0','0','0','1','1'},
            {'1','0','0','0','0','1','0','0','0','0','0','0','1','0','0','0','0','0','1','1'},
            {'0','0','0','0','0','0','1','0','0','0','1','0','1','0','1','1','0','1','0','1'},
            {'1','0','0','1','0','0','0','0','0','0','1','0','0','0','0','0','1','1','1','1'},
            {'0','0','0','1','1','0','0','0','0','0','0','0','0','1','0','0','0','1','0','0'}
        };
        attempt = new Solution().numIslands(grid);
        assert attempt == 45 : "Expected 45, but got " + attempt;


    }
}