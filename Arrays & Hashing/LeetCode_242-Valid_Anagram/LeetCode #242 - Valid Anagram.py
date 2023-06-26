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
	# T&M: O(n), where n is size of s & t
	def isAnagram(self, s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
		# counting chars into s & t dict
		s_cnt, t_cnt = {}, {}
		for s_char, t_char in zip(s, t):
			s_cnt[s_char] = 1 + s_cnt.get(s_char, 0)
			t_cnt[t_char] = 1 + t_cnt.get(t_char, 0)
		return s_cnt == t_cnt

	# Sorting
	# Time & space complexity: O(n log n)
	# def isAnagram(self, s: str, t: str) -> bool:
	# 	if sorted(s) == sorted(t):
	# 		return True
	# return False

s = Solution()

# Ex1
ans = s.isAnagram(s = "anagram", t = "nagaram")
assert ans == True, f'Expected True but got {ans}'
# Ex2
ans = s.isAnagram(s = "rat", t = "car")
assert ans == False, f'Expected False but got {ans}'
# Ex3
ans = s.isAnagram(s = "Hello", t = "Hell")
assert ans == False, f'Expected False but got {ans}'