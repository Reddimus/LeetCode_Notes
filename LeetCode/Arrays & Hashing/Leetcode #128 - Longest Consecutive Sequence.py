'''
Leetcode #128 - Longest Consecutive Sequence prompt:
Given an unsorted array of integers nums, return the length of the longest 
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
Therefore its length is 4.

Example 2:
Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9
 

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
'''

class Solution:
	def longestConsecutive(self, nums: list[int]) -> int:
		# Time complexity:  O(n)
		# Space complexity: O(n)
		numSet = set(nums)
		longest = 0
		for n in nums:
			# check if its the start of a sequence
			if (n - 1) not in numSet:
				length = 1
				while (n + length) in numSet:
					length += 1
				longest = max(length, longest)
		return longest
	'''
	def longestConsecutive(self, nums: list[int]) -> int:
		# similar algorithm slightly slower because the use of a dictionary
		# Time complexity:  O(n)
		# Space complexity: O(n)
		num_map = {}
		for num in nums:
			num_map[num] = False
		longest_sequence = 0
		for num in num_map:
			# check to see if key has been visited (True / False)
			if num_map[num]:
				continue
			current_sequence = 1
			left, right = num - 1, num + 1
			while left in num_map:
				num_map[left] = True
				left -= 1
				current_sequence += 1
			while right in num_map:
				num_map[right] = True
				right += 1
				current_sequence += 1
			longest_sequence = max(longest_sequence, current_sequence)
		return longest_sequence
	'''
	'''
	def longestConsecutive(self, nums: list[int]) -> int:
		# Same algorithm but more computationaly heavy due to while loops and functions used
		# Time complexity:	O(n)
		# Space complexity: O(n)
		cons_set = set(nums)
		cons_count = 0
		while cons_set:
			num = next(iter(cons_set))
			temp_count = 0
			l_nums, r_nums = num - 1, num + 1
			cons_set.remove(num)
			temp_count += 1
			while l_nums in cons_set:
				cons_set.remove(l_nums)
				l_nums -= 1
				temp_count += 1
			while r_nums in cons_set:
				cons_set.remove(r_nums)
				r_nums += 1
				temp_count += 1
			if temp_count > cons_count:
				cons_count = temp_count
		return cons_count
	'''

# Ex 1
assert Solution().longestConsecutive(nums = [100, 4, 200, 1, 3, 2]) == 4

# Ex 2
assert Solution().longestConsecutive(nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
