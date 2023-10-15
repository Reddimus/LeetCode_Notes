import java.util.*;
import java.io.*;

class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        
    }
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