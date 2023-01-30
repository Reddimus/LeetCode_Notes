'''
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
 
Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), 
where n is the array's size.
'''

class Solution:
	def topKFrequent(self, nums: list[int], k: int) -> list[int]:
		# Time complexity: 	O(3n + k) = O(3n + n) = O(4n) = O(n), where k <= n
		# Space Complexity: O(2n) = O(n)
		# count occurences of nums into a hash table
		count_table = {}
		for num in nums:
			count_table[num] = 1 + count_table.get(num, 0)

		# re-sort nums into a freq arr
		freq = [[] for idx in range(len(nums) + 1)]
		for num, count in count_table.items():
			# will put nums from least -> greatest freq
			freq[count].append(num)	

		# iterate through freq arr from highest to lowest freqs
		most_freq = []
		for idx in range(len(freq) - 1, 0, -1):
			# empty [] will pass in for loop
			# append most_freq nums until k is reached
			for num in freq[idx]:
				most_freq.append(num)
				if len(most_freq) == k:
					return most_freq

# Ex 1
assert Solution().topKFrequent(nums = [1, 1, 1, 2, 2, 3], k = 2) == [1, 2]

# Ex 2
assert Solution().topKFrequent(nums = [1], k = 1) == [1]

# Test Case 3
assert Solution().topKFrequent(nums = [4, 1, 4, 2, 2, 3, 4], k = 2) == [4, 2]

# Test Case 4
assert Solution().topKFrequent(nums = [1, 2, 3, 4, 5, 6, 7], k = 4) == [1, 2, 3, 4]

# Test Case 5
assert Solution().topKFrequent(nums = [5, 5, 5, 4, 4, 4, 3, 3, 3], k = 3) == [5, 4, 3]

# Test Case 6
assert Solution().topKFrequent(nums = [5, 5, 5, 5, 5, 6, 7, 8, 9], k = 2) == [5, 6]

# Test Case 7
assert Solution().topKFrequent(nums = [-1, -1, -1, -1, -1, -2], k = 1) == [-1]

# Test Case 8
assert Solution().topKFrequent(nums = [1, 1, 1, 1, 1, 1], k = 1) == [1]