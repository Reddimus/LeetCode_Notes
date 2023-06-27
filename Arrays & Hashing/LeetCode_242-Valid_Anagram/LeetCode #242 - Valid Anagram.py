'''
Leetcode #242 - Valid Anagram prompt:

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
'''

class Solution:
	# Char counting/Hash map approach
	# T & M: O(n), where n is size of largest string of s or t
	def isAnagram(self, s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
		# counting chars into s & t dict
		s_cnt, t_cnt = {}, {}
		for s_char, t_char in zip(s, t):
			s_cnt[s_char] = 1 + s_cnt.get(s_char, 0)
			t_cnt[t_char] = 1 + t_cnt.get(t_char, 0)
		return s_cnt == t_cnt

	# Sorting approach
	# T: O(n log n), M: O(1), where n is size of largest string of s or t
	# def isAnagram(self, s: str, t: str) -> bool:
	# 	if sorted(s) == sorted(t):
	# 		return True
	# return False

s = Solution()

# Ex1
attempt = s.isAnagram(s = "anagram", t = "nagaram")
assert attempt == True, f'Expected True but got {attempt}'
# Ex2
ans = s.isAnagram(s = "rat", t = "car")
assert attempt == False, f'Expected False but got {attempt}'
# Ex3
ans = s.isAnagram(s = "Hello", t = "He")
assert attempt == False, f'Expected False but got {attempt}'