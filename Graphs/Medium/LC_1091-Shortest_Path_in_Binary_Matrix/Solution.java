import java.util.*;
import java.io.*;

// Matrix Graphs - Breadth First Search (BFS) approach
// T: O(n^2), M: O(n^2), where n is the number of rows and columns in the grid
class Solution {
    private static class Indices {
        final int row, col;
        Indices(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
    int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;    // n * n grid, n == rows == cols
        if (grid[0][0] == 1 || grid[n-1][n-1] == 1) 
            return -1;

        Queue<Indices> qCell = new LinkedList<>();  // queue cell indices
        qCell.add(new Indices(0, 0));
        Queue<Integer> qLen = new LinkedList<>();   // accompany queued cells with length
        qLen.add(1);
        grid[0][0] = 1;                             // visited cell
        Indices[] directions = {new Indices(1, 0),      // down
                                new Indices(-1, 0),     // up
                                new Indices(0, 1),      // right
                                new Indices(0, -1),     // left
                                new Indices(1, 1),      // down-right
                                new Indices(-1, -1),    // up-left
                                new Indices(1, -1),     // down-left
                                new Indices(-1, 1)};    // up-right

        // While there is a valid path queued or goal not reached
        while (!qCell.isEmpty()) {
            Indices currCell = qCell.poll();
            int length = qLen.poll();
            if (currCell.row == n-1 && currCell.col == n-1) 
                return length;

            // Explore if neighboring nodes are a valid path
            for (Indices dir : directions) {
                int nghbrRow = dir.row + currCell.row;
                int nghbrCol = dir.col + currCell.col;
                // if neighboring cell is not blocked & has not been visited
                if ((-1 < nghbrRow && nghbrRow < n) &&
                (-1 < nghbrCol && nghbrCol < n) &&
                grid[nghbrRow][nghbrCol] == 0) {
                    grid[nghbrRow][nghbrCol] = 1;   // visited cell
                    qCell.add(new Indices(nghbrRow, nghbrCol));
                    qLen.add(length+1);
                }
            }
        }

        return -1;
    }
}

class TestCases {
    public static void main (String[] args) {
        // In terminal:
        // Compile:     "javac Solution.java"
        // Test cases:  "java -ea TestCases"
        int attempt;
        int[][] grid;

        // Example 1:
        grid = new int[][] {{0,1}, 
                            {1,0}};
        attempt = new Solution().shortestPathBinaryMatrix(grid);
        assert attempt == 2 : "Expected 2, but got " + attempt;

        // Example 2:
        grid = new int[][] {{0,0,0}, 
                            {1,1,0}, 
                            {1,1,0}};
        attempt = new Solution().shortestPathBinaryMatrix(grid);
        assert attempt == 4 : "Expected 4, but got " + attempt;

        // Test case 3:
        grid = new int[][] {{1,0,0}, 
                            {1,1,0}, 
                            {1,1,0}};
        attempt = new Solution().shortestPathBinaryMatrix(grid);
        assert attempt == -1 : "Expected -1, but got " + attempt;

        // Test Case 4:
        grid = new int[][] {{0}};
        attempt = new Solution().shortestPathBinaryMatrix(grid);
        assert attempt == 1 : "Expected 1, but got " + attempt;

        // Test Case 5:
        grid = new int[][] {{1}};
        attempt = new Solution().shortestPathBinaryMatrix(grid);
        assert attempt == -1 : "Expected -1, but got " + attempt;

        // Test Case 6:
        grid = new int[][] {{0,0,0,0,0,0,1}, 
                            {1,1,1,1,1,0,1}, 
                            {1,0,0,1,1,0,0}, 
                            {0,1,1,0,1,0,1}, 
                            {0,1,1,1,0,0,1}, 
                            {0,1,1,1,1,1,1}, 
                            {0,0,0,0,0,0,0}};
        attempt = new Solution().shortestPathBinaryMatrix(grid);
        assert attempt == 21 : "Expected 21, but got " + attempt;
    }
}