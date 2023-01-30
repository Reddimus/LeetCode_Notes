'''
Leetcode #424 Longest Repeating Character Replacement prompt:

You are given a string s and an integer k. You can choose any character 
of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter 
you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 
Constraints:
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
'''

class Solution:
    # Time complexity: 	O(n)
    # Space complexity: O(n)
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0

        l_ptr = 0
        maxf_char = 0
        for r_ptr in range(len(s)):
            # count r_char into hashmap
            count[s[r_ptr]] = 1 + count.get(s[r_ptr], 0)
            # store most freq char from hashmap
            maxf_char = max(maxf_char, count[s[r_ptr]])

            # if len_window - most freq char > char replacements
            if (r_ptr - l_ptr + 1) - maxf_char > k:  # shrink window & count
                count[s[l_ptr]] -= 1
                l_ptr += 1

            # store biggest len_window between past substring windows to current
            longest = max(longest, r_ptr - l_ptr + 1)
        return longest

    '''
    # Time complexity:  O(26n) = O(n)
    # Space complexity: O(n)
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0

        l_ptr = 0
        for r_ptr in range(len(s)):
            # count r_char into hashmap
            count[s[r_ptr]] = 1 + count.get(s[r_ptr], 0)
            # if len_window - most_freq_char > char_replacements (to many chars to replace)
            if (r_ptr - l_ptr + 1) - max(count.values()) > k: # decrease sliding window & hashmap
                count[s[l_ptr]] -= 1
                l_ptr += 1
            # store biggest len_window
            longest = max(longest, r_ptr - l_ptr + 1)
        return longest
    '''

# Ex 1
assert Solution().characterReplacement(s = "ABAB", k = 2) == 4

# Ex 2
assert Solution().characterReplacement(s = "AABABBA", k = 1) == 4

# Test case 3
assert Solution().characterReplacement(s = "AAAAAAA", k = 7) == 7

# Test case 4
assert Solution().characterReplacement(s = "A", k = 0) == 1