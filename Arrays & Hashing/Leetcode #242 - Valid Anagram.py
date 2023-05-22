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
	# Counting char
	# Time & space complexity: O(n)
	def isAnagram(self, s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
		# counting chars into s & t dict
		s_dict, t_dict = {}, {}
		for idx in range(len(s)):
			s_dict[s[idx]] = 1 + s_dict.get(s[idx], 0)
			t_dict[t[idx]] = 1 + t_dict.get(t[idx], 0)
		return s_dict == t_dict

	# Sorting
	# Time & space complexity: O(n log n)
	# def isAnagram(self, s: str, t: str) -> bool:
	# 	if sorted(s) == sorted(t):
	# 		return True
	# return False

# Ex 1
assert Solution().isAnagram(s = "anagram", t = "nagaram") == True

# Ex 2
assert Solution().isAnagram(s = "rat", t = "car") == False
