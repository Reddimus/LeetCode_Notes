'''
Leetcode #49 - Group Anagrams prompt:

Given an array of strings strs, group the anagrams together. You can return 
the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.


Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

class Solution:
	# Array char count method

	# return an array that represents an alphabet with char cnts
	# T: O(s), M: O(s), where s size of string
	def cntChars(self, string: str) -> list[int]:
		char_cnt = [0] * 26
		for char in string:
			alpha_idx = ord('a') - ord(char.lower())
			char_cnt[alpha_idx] += 1
		return tuple(char_cnt)

	# T: O(n * s), M: O(n * s), where n is size of strs & s size of indiv str
	def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
		anagrams = {}
		for string in strs:
			char_cnt = self.cntChars(string)
			anagrams[char_cnt] = anagrams.get(char_cnt, []) + [string]
		return list(anagrams.values())

	'''
	# Sorting approach
	# T: O(n * s log s), M: O(n), where n is size of strs & s size of indiv str
	def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
		anagrams = {}
		for string in strs:
			sorted_str = ''.join(sorted(string))
			anagrams[sorted_str] = anagrams.get(sorted_str, []) + [string]
		return list(anagrams.values())
	'''

sol = Solution()

# Testcase 1
attempt = sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])
ans = [["bat"],["nat","tan"],["ate","eat","tea"]]
assert attempt == ans or [["eat","tea","ate"],["tan","nat"],["bat"]], f'Expected {ans} but got {attempt}'

# Testcase 2
attempt = sol.groupAnagrams(strs = [""])
ans = [[""]]
assert attempt == ans, f'Expected {ans} but got {attempt}'

# Testcase 3
attempt = sol.groupAnagrams(strs = ["a"])
ans = [["a"]]
assert attempt == ans, f'Expected {ans} but got {attempt}'
