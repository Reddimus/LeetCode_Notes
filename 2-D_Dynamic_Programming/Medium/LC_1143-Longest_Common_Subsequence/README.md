# LeetCode #1143 - Longest Common Subsequence

https://leetcode.com/problems/longest-common-subsequence/description/

### Difficulty: `Medium`

Given two strings `text1` and `text2`, return the length of their longest **common subsequence**. If there is no **common subsequence**, return 0.

A **subsequence** of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters.

* For example, `"ace"` is a subsequence of `"abcde"`.

A **common subsequence** of two strings is a subsequence that is common to both strings.

### Example 1:
Input: 
```
text1 = "abcde", text2 = "ace"
```
Output: 
```
3
```
Explanation: The longest common subsequence is "ace" and its length is 3.

### Example 2:
Input: 
```
text1 = "abc", text2 = "abc"
```
Output: 
```
3
```
Explanation: The longest common subsequence is "abc" and its length is 3.

### Example 3:
Input: 
```
text1 = "abc", text2 = "def"
```
Output: 
```
0
```
Explanation: There is no such common subsequence, so the result is 0.

## Constraints

* `1 <= text1.length, text2.length <= 1000`
* `text1` and `text2` consist of only lowercase English characters.

### Hints
- Try dynamic programming. Where text1 chars & text2 chars are the axes of the 2-D array.
- If a char in text1 and text2 match, then it is part of the LCS and we count up by 1.

# Solution Explanation

https://github.com/Reddimus/LeetCode_Notes/tree/main/2-D_Dynamic_Programming/Medium/LC_1143-Longest_Common_Subsequence

### Intuition
The Longest Common Subsequence (LCS) problem is a textbook example of dynamic programming. The solution can be implemented either via a top-down or a bottom-up approach. A 2-D array `dp` serves as a memoization table that helps us keep track of the length of the longest subsequence found so far. When characters in both strings match, we update our `dp` table by incrementing the count by *1 plus the length of the previously matched subsequence*. In case of a mismatch, we *carry forward the maximum subsequence length found until that point.*

### Steps:
1. Initialize a 2-D array `dp` of size `m+1` by `n+1` with all values set to `0`.
2. Iterate through each charcter in `text1` and `text2`.
    - If the characters are equal then set `dp[i][j] = 1 + dp[previously matched subsequence i][previously matched subsequence j]`.
    - If the characters are not equal find the maximum of `dp[max carried over i][j]` and `dp[i][max carried over j]` and set `dp[i][j]` to that value.
3. Return `dp[0][0]` if you used the bottom up approach or `dp[m][n]` if you used the top down approach.

### Time & Space complexity:
**Time:** `O(m*n)`  
**Space:** `O(m*n)`  

Where `n` is the number of characters in `text1` and `m` is the number of characters in `text2`.

### Python Code:
```python
class Solution:
    # 2-D Dynamic Programming - Bottom up approach
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        chars1, chars2 = len(text1), len(text2)
        dp = [[0] * (chars2+1) for row in range(chars1+1)]

        for c1 in reversed(range(chars1)):
            for c2 in reversed(range(chars2)):
                if text1[c1] == text2[c2]:
                    dp[c1][c2] = 1 + dp[c1+1][c2+1]
                else:
                    dp[c1][c2] = max(dp[c1+1][c2], dp[c1][c2+1])
        
        return dp[0][0]

    '''
    # 2-D Dynamic Programming - Top Down Approach
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        chars1, chars2 = len(text1), len(text2)
        dp = [[0] * (chars2+1) for row in range(chars1+1)]
        
        for c1 in range(1, chars1+1):
            for c2 in range(1, chars2+1):
                if text1[c1-1] == text2[c2-1]:
                    dp[c1][c2] = 1 + dp[c1-1][c2-1]
                else:
                    dp[c1][c2] = max(dp[c1-1][c2], dp[c1][c2-1])
        
        return dp[chars1][chars2]
    '''
```

### C++ Code:
```cpp
```

### Java Code:
```java
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
```