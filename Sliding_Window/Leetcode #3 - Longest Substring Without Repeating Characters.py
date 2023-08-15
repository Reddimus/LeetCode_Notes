'''
Leetcode #3 - Longest Substring Without Repeating Characters prompt:

Given a string s, find the length of the longest substring without 
repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence 
and not a substring.

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
	# Time and space complexity: O(n)
	def lengthOfLongestSubstring(self, s: str) -> int:
		char_set = set()
		l_ptr = 0
		longest = 0

		for r_ptr in range(len(s)):
			while s[r_ptr] in char_set:
				char_set.remove(s[l_ptr])
				l_ptr += 1
			char_set.add(s[r_ptr])
			longest = max(longest, r_ptr - l_ptr + 1)
		return longest



# Ex 1
assert Solution().lengthOfLongestSubstring(s = "abcabcbb") == 3

# Ex 2
assert Solution().lengthOfLongestSubstring(s = "bbbbb") == 1

# Ex 3
assert Solution().lengthOfLongestSubstring(s = "pwwkew") == 3

# Test case 4
assert Solution().lengthOfLongestSubstring(s = "1432kno4,./;'[]-=") == 15

# Test case 5
assert Solution().lengthOfLongestSubstring(s = ",,,,") == 1

# Test case 6
assert Solution().lengthOfLongestSubstring(s = "abcdefgh") == 8

# Test case 7
assert Solution().lengthOfLongestSubstring(s = "a") == 1

# Test case 8 
assert Solution().lengthOfLongestSubstring(s = "dvdf") == 3

# Test case 9
assert Solution().lengthOfLongestSubstring(s = "abba") == 2
