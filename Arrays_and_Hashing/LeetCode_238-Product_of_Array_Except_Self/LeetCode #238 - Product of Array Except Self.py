'''
Leetcode #238 - Product of Array Except Self Prompt:
Easy

Given an integer array nums, return an array answer such that answer[i] is 
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
integer.

You must write an algorithm that runs in O(n) time and without using the 
division operation.

Example 1:
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Example 2:
Input: nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]

Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 
32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)
'''

# Prefix and Postfix arrays

class Solution:
	# T: O(n), M: O(1), where n is the length of nums
	def productExceptSelf(self, nums: list[int]) -> list[int]:
		pes_nums = [1] * len(nums)
  
		# Fill pes_nums with prefix products
		prefix = 1
		for idx in range(len(nums)):
			# starts with a static 1 and ends with second to last prefix product
			pes_nums[idx] = prefix
			prefix *= nums[idx]
		
		# Fill pes_nums with postfix products ontop of prefix products
		postfix = 1
		for idx in range(len(nums) - 1, -1, -1):
			# starts from right to left with same element and ends with second to last postfix product
			pes_nums[idx] *= postfix
			postfix *= nums[idx]

		return pes_nums

	'''
	# Expanded approach (more memory usage)
	# T & M: O(n), where n is the length of nums
	def productExceptSelf(self, nums: list[int]) -> list[int]:
		prefix, pre_arr = 1, [0] * len(nums)
		postfix, post_arr = 1, [0] * len(nums)
		for idx, num in enumerate(nums):
			prefix *= num
			pre_arr[idx] = prefix

			postfix *= nums[-idx - 1]
			post_arr[-idx - 1] = postfix

		print("pre_arr:", pre_arr)
		print("post_arr:", post_arr)

		pes_nums = []
		for idx in range(len(nums)):
			if idx != 0 and idx != len(nums) - 1:
				pes_nums.append(pre_arr[idx - 1] * post_arr[idx + 1])
			elif idx == 0:
				pes_nums.append(post_arr[idx + 1])
			elif idx == len(nums) - 1:
				pes_nums.append(pre_arr[idx - 1])
			print(pes_nums)
		return pes_nums
	'''

sol = Solution()
# Ex 1
attempt = sol.productExceptSelf([1, 2, 3, 4])
assert attempt == [24, 12, 8, 6], f'Expected: [24, 12, 8, 6], but got: {attempt}'
# Ex 2
attempt = sol.productExceptSelf([-1, 1, 0, -3, 3])
assert attempt == [0, 0, 9, 0, 0], f'Expected: [0, 0, 9, 0, 0], but got: {attempt}'
# Test case 3
attempt = sol.productExceptSelf([1, 2])
assert attempt == [2, 1], f'Expected: [2, 1], but got: {attempt}'