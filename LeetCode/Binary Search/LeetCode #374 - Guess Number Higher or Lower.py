'''
LeetCode # 374 - Guess Number Higher or Lower prompt:

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I 
picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three 
possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked. 

Example 1:
Input: n = 10, pick = 6
Output: 6

Example 2:
Input: n = 1, pick = 1
Output: 1

Example 3:
Input: n = 2, pick = 1
Output: 1

Constraints:
1 <= n <= 2^31 - 1
1 <= pick <= n
'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
	# __init__ should be hidden
	def __init__(self, pick):
		self.pick = pick

	# Solution starts here
	# Time complexity: 	O(log n)
	# Space complexity: O(1)
	def guessNumber(self, n: int) -> int:
		l_ptr, r_ptr = 1, n
		# keep guessing until it is right
		while True:
			# midpoint = left_ptr + half dist
			mid = l_ptr + ((r_ptr - l_ptr) // 2)
			my_guess = self.guess(num = mid)
			if my_guess == 1:
				l_ptr = mid + 1
			elif my_guess == -1:
				r_ptr = mid - 1
			else:
				return mid

	# guess func should be hidden
	def guess(self, num: int) -> int:
		pick = self.pick
		if num < pick: 
			return 1
		elif num > pick:
			return -1
		else:
			return 0

# Ex 1:
assert Solution(pick = 6).guessNumber(n = 10) == 6

# Ex 2:
assert Solution(pick = 1).guessNumber(n = 1) == 1

# Ex 3:
assert Solution(pick = 1).guessNumber(n = 2) == 1
