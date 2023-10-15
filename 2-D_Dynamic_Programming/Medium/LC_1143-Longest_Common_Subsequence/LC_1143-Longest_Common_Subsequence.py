class Solution:
    # 2-D Dynamic Programming - Bottom up approach
    # T&M: O(m*n), where m = text1 chars, n = text2 chars
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
    # T&M: O(m*n), where m = text1 chars, n = text2 chars
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

sol = Solution()

# Ex1
attempt = sol.longestCommonSubsequence("abcde", "ace")
assert attempt == 3, f'Expected 3, but got {attempt}'
# Ex2
attempt = sol.longestCommonSubsequence("abc", "abc")
assert attempt == 3, f'Expected 3, but got {attempt}'
# Ex3
attempt = sol.longestCommonSubsequence("abc", "def")
assert attempt == 0, f'Expected 0, but got {attempt}'
