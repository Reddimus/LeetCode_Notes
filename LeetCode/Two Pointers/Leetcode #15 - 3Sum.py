'''
Leetcode #15 - 3Sum prompt:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0. 

Constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
'''

class Solution:
	# Time complexity: 	O(n log n) + O(n^2) = O(n^2)
	# Space complexity: O(1)
	def threeSum(self, nums: list[int]) -> list[list[int]]:
		unique_comb = []
		nums.sort()

		for idx, num in enumerate(nums):
			if idx > 0 and num == nums[idx - 1]:
				continue	# pass w/ else:

			# we can use hashmaps however using 2 ptrs for 2 sum uses less memory
			l_ptr, r_ptr = idx + 1, len(nums) - 1
			while l_ptr < r_ptr:
				threeSum = num + nums[l_ptr] + nums[r_ptr]
				# sorted therefore we can decrease or increase 2sum by iterating
				if threeSum > 0: 	# decrease total
					r_ptr -= 1
				elif threeSum < 0: 	# increase total
					l_ptr += 1
				else:
					unique_comb.append([num, nums[l_ptr], nums[r_ptr]])
					l_ptr += 1
					while nums[l_ptr] == nums[l_ptr - 1] and l_ptr < r_ptr:
						l_ptr += 1	#r_ptr will be updated later if duplicate
		return unique_comb

# Ex 1
assert Solution().threeSum(nums = [-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]

# Ex 2
assert Solution().threeSum(nums = [0, 1, 1]) == []

# Ex 3
assert Solution().threeSum(nums = [0, 0, 0]) == [[0, 0, 0]]

# Ex 4
assert Solution().threeSum(nums = [1, 2, -3, -2, -1]) == [[-3, 1, 2]]

# Ex 5
assert Solution().threeSum(nums = [-1, -1, 0, 2, 2]) == [[-1, -1, 2]]

# Ex 6
assert Solution().threeSum(nums = [-1, 0, 1, 0]) == [[-1, 0, 1]]

# Ex 7
assert Solution().threeSum(nums = [1, 2, 3, -6]) == []

# Ex 8
assert Solution().threeSum(nums = [-1, -1, -1, 0, 1, 2]) == [[-1, -1, 2], [-1, 0, 1]]