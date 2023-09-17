class Solution {
    // T: O(n), M: O(1), where n is amount of steps
    public int minCostClimbingStairs(int[] cost) {
        // Bottom-up approach; start from 3rd step
        for (int i = 2; i < cost.length; i++) {
            cost[i] += Math.min(cost[i - 1], cost[i - 2]);
        }
        return Math.min(cost[cost.length - 1], cost[cost.length - 2]);
    }
    
    /*
    // T: O(n), M: O(1), where n is amount of steps
    public int minCostClimbingStairs(int[] cost) {
        // Top-down approach; start from 3rd to last step
        for (int i = cost.length - 3; i >= 0; i--) {
            cost[i] += Math.min(cost[i + 1], cost[i + 2]);
        }
        return Math.min(cost[0], cost[1]);
    }
    */
}

class TestCases {
    public static void main(String[] args) {
        // In terminal:
        // Compile:     "javac Solution.java"
        // Test cases:  "java -ea TestCases"
        Solution sol = new Solution();
        int attempt;
        int[] cost;

        // Ex 1
        cost = new int[]{10, 15, 20};
        attempt = sol.minCostClimbingStairs(cost);
        assert attempt == 15 : "Expected 15, but got " + attempt;
        // Ex 2
        cost = new int[]{1, 100, 1, 1, 1, 100, 1, 1, 100, 1};
        attempt = sol.minCostClimbingStairs(cost);
        assert attempt == 6 : "Expected 6, but got " + attempt;
    }
}