'''
LeetCode #278 - First Bad Version prompt:

You are a product manager and currently leading a team to develop a 
new product. Unfortunately, the latest version of your product fails 
the quality check. Since each version is developed based on the 
previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out 
the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether 
version is bad. Implement a function to find the first bad version. 
You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1

Constraints:
1 <= bad <= n <= 2^31 - 1
'''

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
	# __init__ should be hidden
	def __init__(self, bad):
		self.bad = bad

	# isBadVersion should be hidden
	def isBadVersion(self, guess: int) -> bool:
		ans = self.bad
		if guess < ans:
			return False
		elif guess > ans:
			return True
		else:
			return True

	# Solution here:
	# Time complexity: 	O(log n)
	# Space complexity: O(1)
	def firstBadVersion(self, n: int) -> int:
		l_ptr, r_ptr = 1, n
		while l_ptr < r_ptr:
			mid = (l_ptr + r_ptr) // 2
			# if mid is bad/ True
			if self.isBadVersion(guess = mid):
				r_ptr = mid
			# if mid is good/ false
			else:
				l_ptr = mid + 1
		return l_ptr

	'''
	# Same time & space complexity, computationally more heavy per iteration due to checking 2 nums
	# Time complexity: 	O(log n)
	# Space complexity: O(1)
	def firstBadVersion(self, n: int) -> int:
		l_ptr, r_ptr = 1, n
		# look for [false, true]
		while True:
			mid = l_ptr + (r_ptr - l_ptr) // 2
			guess_arr = [self.isBadVersion(guess = mid), self.isBadVersion(guess = mid + 1)]
			if guess_arr == [False, False]:
				l_ptr = mid + 2
			elif guess_arr == [True, True]:
				r_ptr = mid - 2
			# check for [false, true]
			elif guess_arr[1] == True:
				return mid + 1
			# guess_arr can be [True, False] if mid + 1 > len(arr)
			else:
				return mid
	'''

# Ex 1:
assert Solution(bad = 4).firstBadVersion(n = 5) == 4

# Ex 2:
assert Solution(bad = 1).firstBadVersion(n = 1) == 1

# Testcase 3:
assert Solution(bad = (2 ** 31) - 1).firstBadVersion(n = (2 ** 31) - 1) == (2 ** 31) - 1