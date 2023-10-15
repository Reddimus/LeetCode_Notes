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
- 

# Solution Explanation

https://github.com/Reddimus/LeetCode_Notes/tree/main/2-D_Dynamic_Programming/Medium/LC_1143-Longest_Common_Subsequence

## Approach: 

### Intuition

### Steps:
1. 

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
```