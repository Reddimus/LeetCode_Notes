'''
Leetcode #271 - Encode and Decode Strings Prompt:
Design an algorithm to encode a list of strings to a string. The encoded 
string is then sent over the network and is decoded back to the original 
list of strings.

Please implement encode and decode

Example 1:
Input: 	["lint", "code", "love", "you"]
Output: ["lint", "code", "love", "you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example 2:
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
'''

class Solution:
	# Time and space complexity: O(n)
	"""
	@param: strs: a list of strings
	@return: encodes a list of strings to a single string.
	"""

	def encode(self, strs: list[str]) -> str:
		encoded_str = ""
		for string in strs:
			encoded_str += str(len(string)) + "#" + string
		return encoded_str

	"""
	@param: string: A string
	@return: decodes a single string to a list of strings
	"""

	def decode(self, string: str) -> list[str]:
		decoded_arr, idx = [], 0
		while idx < len(string):
			j = idx
			while string[j] != "#":		# len(string) can be > 9
				j += 1
			length = int(string[idx:j])
			decoded_arr.append(string[j + 1 : j + 1 + length])
			idx = j + 1 + length
		return decoded_arr

# Ex 1
assert Solution().encode(strs = ["lint", "code", "love", "you"]) == "4#lint4#code4#love3#you"
assert Solution().decode(string = "4#lint4#code4#love3#you") == ["lint", "code", "love", "you"]

# Ex 2
assert Solution().encode(strs = ["we", "say", ":", "yes"]) == "2#we3#say1#:3#yes"
assert Solution().decode(string = "2#we3#say1#:3#yes") == ["we", "say", ":", "yes"]

# Test case 3
assert Solution().encode(strs = ["By"]) == "2#By"
assert Solution().decode(string = "2#By") == ["By"]

# Test case 4
assert Solution().encode(strs = ["1"]) == "1#1"
assert Solution().decode(string = "1#1") == ["1"]

# Test case 5
assert Solution().encode(strs = ["1", "5", "6", "9"]) == "1#11#51#61#9"
assert Solution().decode(string = "1#11#51#61#9") == ["1", "5", "6", "9"]
