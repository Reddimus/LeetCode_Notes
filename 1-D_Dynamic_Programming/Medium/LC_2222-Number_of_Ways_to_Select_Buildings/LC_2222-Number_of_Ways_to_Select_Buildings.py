class Solution:
	# T: O(n), M: O(1), where n is the number of stairs
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