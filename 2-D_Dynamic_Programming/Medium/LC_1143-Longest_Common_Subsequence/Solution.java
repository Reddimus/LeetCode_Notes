class Solution {
    // 2-D Dynamic Programming - Bottom up approach
    // T&M: O(m*n), where m = text1 chars, n = text2 chars
    public int longestCommonSubsequence(String text1, String text2) {
        int chars1 = text1.length(), chars2 = text2.length();
        int[][] dp = new int[chars1 + 1][chars2 + 1];
        for (int c1 = chars1 - 1; c1 >= 0; --c1) {
            for (int c2 = chars2 - 1; c2 >= 0; --c2) {
                if (text1.charAt(c1) == text2.charAt(c2))
                    dp[c1][c2] = 1 + dp[c1+1][c2+1];
                else
                    dp[c1][c2] = Math.max(dp[c1+1][c2], dp[c1][c2+1]);
            }
        }
        return dp[0][0];
    }

    /*
    // 2-D Dynamic Programming - Top down approach
    // T&M: O(m*n), where m = text1 chars, n = text2 chars
    public int longestCommonSubsequence(String text1, String text2) {
        int chars1 = text1.length(), chars2 = text2.length();
        int[][] dp = new int[chars1 + 1][chars2 + 1];
        for (int c1 = 1; c1 <= chars1; ++c1) {
            for (int c2 = 1; c2 <= chars2; ++c2) {
                if (text1.charAt(c1-1) == text2.charAt(c2-1))
                    dp[c1][c2] = 1 + dp[c1-1][c2-1];
                else
                    dp[c1][c2] = Math.max(dp[c1-1][c2], dp[c1][c2-1]);
            }
        }
        return dp[chars1][chars2];
    }
    */
}

class TestCases {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int attempt;

        // Ex1
        attempt = sol.longestCommonSubsequence("abcde", "ace");
        assert attempt == 3 : "Expected 3, but got " + attempt;
        // Ex2
        attempt = sol.longestCommonSubsequence("abc", "abc");
        assert attempt == 3 : "Expected 3, but got " + attempt;
        // Ex3
        attempt = sol.longestCommonSubsequence("abc", "def");
        assert attempt == 0 : "Expected 0, but got " + attempt;
    }
}