class Solution {
    // Dynamic programming w/ 2 variables approach
    // T: O(n), M: O(1)
    public int fib(int n) {
        if (n <= 1)
            return n;
        
        // start from 2
        int n0 = 0, n1 = 1;
        for (int num = 2; num <= n; num++) {
            int temp = n0 + n1;
            n0 = n1;
            n1 = temp;
        }
        return n1;
    }

    /*
    // Dynamic programming w/ Array approach
    // T: O(n), M: O(n)
    public int fib(int n) {
        if (n <= 1)
            return n;
        
        // start from 2
        int[] dp = new int[n+1];
        dp[1] = 1;
        for (int num = 2; num <= n; num++) {
            dp[num] = dp[num-2] + dp[num-1];
        }
        return dp[n];
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

        // Ex1
        attempt = sol.fib(2);
        assert attempt == 1 : "Expected 1, but got " + attempt;
        // Ex2
        attempt = sol.fib(3);
        assert attempt == 2 : "Expected 2, but got " + attempt;
        // Ex3
        attempt = sol.fib(4);
        assert attempt == 3 : "Expected 3, but got " + attempt;
    }
}