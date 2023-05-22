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

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''
class Solution:
	# n = len(strs), c = chars = len(string), count = 26
	# time complexity: 	O(n * c * 26) = O(n * c)
	# space complexity: O(n)
	def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
		res = {}
		for string in strs:
			count = [0] * 26
			for char in string:
				count[ord(char) - ord("a")] += 1
			# if val not found initialize as []
			# else keep res[tuple(count)] value the same
			res[tuple(count)] = res.get(tuple(count), [])
			res[tuple(count)].append(string)
		# returns all values in the hash table as a list
		return list(res.values())
	'''
	# Collections library
	def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
		import collections
		# Define res as a dictionary with values as a list
		res = collections.defaultdict(list) # mapping charCount to list of Anagrams
		for string in strs:
			count = [0] * 26 # len(alphabet) = a -> z = 26
			for char in string:
				count[ord(char) - ord("a")] += 1
			# In Python, a list cannot be used as a key in a dictionary, but a tuple can.
			res[tuple(count)].append(string)
		print(res)
		return list(res.values())
	'''

	'''
	# n = len(strs), c = chars = len(string)
	# time complexity: O(n * c) + O(n * (n - 1) / 2) = O(n * c) + O(n^2) = O(n^2) 
	# space complexit: O(n)
	def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
		if len(strs) <= 1:
			return [strs]
		# create hash table for each string in the arr and append them to dict_arr
		dict_arr = []
		for string in strs:
			temp_count = {}
			# iterate through each char of the str to count # of chars
			for char in string:
				temp_count[char] = 1 + temp_count.get(char, 0)
			dict_arr.append(temp_count)

		# Use 2 ptrs to compare strings and their respected hash tables
		anagram_arr = []
		ptr_0 = 0
		while ptr_0 != len(strs):
			temp_group = []
			temp_group.append(strs[ptr_0])
			ptr_1 = ptr_0 + 1
			while ptr_1 != len(strs):
				anagram = False
				# if compared dictionary keys & vals are the same then both strings are anagrams
				if dict_arr[ptr_0] == dict_arr[ptr_1]:
					anagram = True
				# if compared strings are anagrams append them to group arr
				if anagram == True:
					temp_group.append(strs[ptr_1])
					strs.pop(ptr_1)
					dict_arr.pop(ptr_1)
				else:
					ptr_1 += 1
			# anagram group ends and is added to anagram_arr (output)
			anagram_arr.append(temp_group)
			ptr_0 += 1
		return anagram_arr
	'''


# Testcase 1
assert Solution().groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]] or [["eat","tea","ate"],["tan","nat"],["bat"]]

# Testcase 2
assert Solution().groupAnagrams(strs = [""]) == [[""]]

# Testcase 3
assert Solution().groupAnagrams(strs = ["a"]) == [["a"]]
