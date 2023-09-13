class Solution:
	# Two pointers method
	# T: O(n), M: O(1), where n is size of s
	def isPalindrome(self, s: str) -> bool:
		lo, hi = 0, len(s) - 1
		# converge pointers and compare
		while lo < hi:
			if not s[lo].isalnum():
				lo += 1
				continue
			if not s[hi].isalnum():
				hi -= 1
				continue
			if s[lo].lower() != s[hi].lower():
				return False
			lo += 1
			hi -= 1
		return True

	'''
	# Other way to iterate two pointers method
	# T: O(n), M: O(1), where n is size of s
	def isPalindrome(self, s: str) -> bool:
		l_idx, r_idx = 0, len(s) - 1
		# converge pointers and compare
		while l_idx < r_idx:
			while l_idx < r_idx and not self.alphanum(s[l_idx]):
				l_idx += 1
			while l_idx < r_idx and not self.alphanum(s[r_idx]):
				r_idx -= 1
			if s[l_idx].lower() != s[r_idx].lower():
				return False
			l_idx += 1
			r_idx -= 1
		return True

	def alphanum(self, char: str) -> bool:
		return (
			"a" <= char.lower() <= "z"
			or '0' <= char <= '9'
			)
	'''

sol = Solution()
# Ex 1
assert sol.isPalindrome(s = "A man, a plan, a canal: Panama") == True, f'Expected True but got False'
# Ex 2
assert sol.isPalindrome(s = "race a car") == False, f'Expected False but got True'
# Ex 3
assert sol.isPalindrome(s = '') == True, f'Expected True but got False'
# My Ex 1
assert sol.isPalindrome(s = "cabbac") == True, f'Expected True but got False'
# My Ex 2
assert sol.isPalindrome(s = "cac") == True, f'Expected True but got False'
# My Ex 3
assert sol.isPalindrome(s = "012210") == True, f'Expected True but got False'
# My Ex 4
assert sol.isPalindrome(s = "04104214") == False, f'Expected False but got True'
# My Ex 5
assert sol.isPalindrome(s = '.,') == True, f'Expected True but got False'
