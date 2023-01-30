'''
Leetcode #11 - Container With Most Water:

You are given an integer array height of length n. There are n vertical lines 
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the 
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7] 	7 * 7 = 49
Output: 49
Explanation: The above vertical lines are represented by array 
[1, 8, 6, 2, 5, 4, 8, 3, 7]. In this case, the max area of water 
(blue section) the container can contain is 49.

Example 2:
Input: height = [1, 1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
'''

class Solution:
	# Time complexity: 	O(n)
	# Space complexity: O(1)
	def maxArea(self, height: list[int]) -> int:
		l_ptr, r_ptr = 0, len(height) - 1
		most_water = 0
		while l_ptr < r_ptr:
			temp_water = min(height[l_ptr], height[r_ptr]) * (r_ptr - l_ptr)
			most_water = max(most_water, temp_water)
			if height[l_ptr] < height[r_ptr]:
				l_ptr += 1
			else:
				r_ptr -= 1
		return most_water


# Ex 1
assert Solution().maxArea(height = [1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

# Ex 2
assert Solution().maxArea(height = [1, 1]) == 1

# Test Case 3
assert Solution().maxArea(height = [1, 1, 1, 100, 100, 1, 1, 1]) == 100

# Test Case 4
assert Solution().maxArea(height = [1] * 100) == 99

# Test Case 5:
assert Solution().maxArea(height = [100, 1, 1, 1, 100, 1, 1, 100]) == 700

# Test Case 6:
assert Solution().maxArea(height = [5, 4, 3, 2, 1]) == 6

# Test Case 7:
assert Solution().maxArea(height = [1, 2, 3, 4, 5]) == 6

# Test Case 8:
assert Solution().maxArea(height = [1, 5, 2, 3, 4]) == 12

# Test Case 9:
assert Solution().maxArea(height = [5, 3, 2, 4, 1]) == 12

# Test Case 10:
assert Solution().maxArea(height = [5, 5, 5, 5, 5]) == 20