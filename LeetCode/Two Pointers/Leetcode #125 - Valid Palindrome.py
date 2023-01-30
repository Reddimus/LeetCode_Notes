'''
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads 
the same forward and backward. Alphanumeric characters include letters 
and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal:
Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Discussion
Solutions
Submissions
Input: s = "race a car"
Output: false
Explanation: "raceacar' is not a palindrome.

Example 3:
Input: s = "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
• 1 <= s. length <= 2 * 105
• S consists only of printable ASCII characters
'''

class Solution:
	# Time complexity: 	O(n)
	# Space complexity: O(1)
	def isPalindrome(self, s: str) -> bool:
		l_idx, r_idx = 0, len(s) - 1
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
	# similar algorithm, VERY close in runtime but a little slower
	# Time complexity: 	O(n)
	# Space complexity: O(1)
	def isPalindrome(self, s: str) -> bool:
		l_idx, r_idx = 0, len(s) - 1
		
		# iterate from left & right side of the str
		while(l_idx < r_idx):	
			# skip non-alphabetical chars or nums
			l_idx = self.skip_char(s, l_idx, reverse = False)
			r_idx = self.skip_char(s, r_idx, reverse = True)
			if s[l_idx].lower() != s[r_idx].lower() and l_idx < r_idx:
				return False
			l_idx += 1
			r_idx -= 1
		return True
		
	def skip_char(self, s: str, idx: int, reverse: bool):
		while ((s[idx].lower() < 'a') or ('z' < s[idx].lower())) and (((s[idx] < '0')) or ('9' < s[idx])):
			# if not alpha char or number skip
			if reverse == False and idx + 1 <= len(s) - 1:
				idx += 1
			elif reverse == True and idx - 1 >= 0:
				idx -= 1
			else:
				break
		return idx
	'''

# My Ex 1
assert Solution().isPalindrome(s = "cabbac") == True

# My Ex 2
assert Solution().isPalindrome(s = "cac") == True

# My Ex 3
assert Solution().isPalindrome(s = "012210") == True

# My Ex 4
assert Solution().isPalindrome(s = "04104214") == False

# My Ex 5
assert Solution().isPalindrome(s = '.,') == True

# Ex 1
assert Solution().isPalindrome(s = "A man, a plan, a canal: Panama") == True

# Ex 2
assert Solution().isPalindrome(s = "race a car") == False

# Ex 3
assert Solution().isPalindrome(s = '') == True
