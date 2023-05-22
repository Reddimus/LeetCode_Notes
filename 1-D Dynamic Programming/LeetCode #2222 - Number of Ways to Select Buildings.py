'''
LeetCode #2222 - Number of Ways to Select Buildings prompt:

You are given a 0-indexed binary string s which represents the types of buildings along a 
street where:

s[i] = '0' denotes that the ith building is an office and
s[i] = '1' denotes that the ith building is a restaurant.
As a city official, you would like to select 3 buildings for random inspection. However, 
to ensure variety, no two consecutive buildings out of the selected buildings can be of 
the same type.

For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings as that 
would form "011" which is not allowed due to having two consecutive buildings of the same type.
Return the number of valid ways to select 3 buildings.

Example 1:
Input: s = "001101"
Output: 6
Explanation: 
The following sets of indices selected are valid:
- [0,2,4] from "001101" forms "010"
- [0,3,4] from "001101" forms "010"
- [1,2,4] from "001101" forms "010"
- [1,3,4] from "001101" forms "010"
- [2,4,5] from "001101" forms "101"
- [3,4,5] from "001101" forms "101"
No other selection is valid. Thus, there are 6 total ways.

Example 2:
Input: s = "11100"
Output: 0
Explanation: It can be shown that there are no valid selections.

Constraints:
3 <= s.length <= 10^5
s[i] is either '0' or '1'.
'''

class Solution:
	# Time complexity: 	O(n)
	# Space complexity: O(1)
	def numberOfWays(self, s: str) -> int:
		print(s)
		# count 0, 1, 01, 10
		z = o = zo = oz = total = 0
		for build in s:
			if build == '0':	# if building is an office
				total += oz		# updated total if there was a complete previous ozo combination
				zo += z			# have zero to complete combination
				o += 1			# need one
			elif build == '1':	# if building is a restaurant
				total += zo		# update total if there was a complete previous zoz combination
				oz += o 		# have one to complete combination
				z += 1			# need zero
		return total

ex1 = Solution().numberOfWays(s = "001101")
assert ex1 == 6, f'Expected {6}, but got {ex1}'

ex2 = Solution().numberOfWays(s = "11100")
assert ex2 == 0, f'Expected {0}, but got {ex2}'