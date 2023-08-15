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
		print(nums, k)
		count, max_count = {}, 0
		for num in nums:
			count[num] = 1 + count.get(num, 0)
			max_count = max(max_count, count[num])
		print(count)
		if len(count) <= k:
			return list(count.keys())
		# re-sort nums into a freq arr
		freq = [[] for idx in range(max_count + 1)]
		print(freq)
		for num, count in count.items():
			# will put nums from least -> greatest freq
			freq[count].append(num)	
			print(freq)

		# iterate through freq arr from highest to lowest freqs
		most_freq = []
		for idx in range(len(freq) - 1, 0, -1):
			# empty [] will pass in for loop
			# append most_freq nums until k is reached
			for num in freq[idx]:
				most_freq.append(num)
				if len(most_freq) == k:
					print(most_freq, "\n")
					return most_freq

    # # Time complexity:  O(n log n), where n is size of nums arr
    # # Space complexity: O(n)
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     # Count the amount of freq elements
    #     count = {}
    #     for num in nums:
    #         count[num] = 1 + count.get(num, 0)
    #     if len(count) <= k:
    #         return list(count.keys())
    #     # Sort the count map by descending value order and append k most freq nums
    #     most_freq = []
    #     for iter, (key, val) in enumerate(sorted(count.items(), key=lambda item: item[1], reverse=True)):
    #         most_freq.append(key)
    #         if iter + 1 >= k:
    #             return most_freq

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