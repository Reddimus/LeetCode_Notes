'''
Leetcode #20 - Valid Parenthesis prompt:
Given a string s containing just the characters '(', ')', '{', '}', 
'[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
'''

class Solution:
	# Time complexity: 	O(n)
	# Space complexity: O(n)
	def isValid(self, s: str) -> bool:
		parenth_map = {")": "(", "]": "[", "}": "{"}
		# if first char == end_parenth or last char == open_parenth
		if s[0] in parenth_map or s[-1] not in parenth_map:
			return False
		# opening parenthesis stack
		stack = []
		for char in s:
			# if char is an opening parenthesis
			if char not in parenth_map:
				stack.append(char)
				continue
			# if stack is empty or last char in stack is mismatching opening parenth
			if not stack or stack[-1] != parenth_map[char]:
				return False
			# pop top of opening parenthesis stack
			stack.pop()
		return not stack
	'''
	# Time complexity: 	O(n)
	# Space complexity: O(n)
	def isValid(self, s: str) -> bool:
		stack = []
		closeToOpen = {")": "(", "]": "[", "}": "{"}

		for char in s:
			if char in closeToOpen:
				if stack and stack[-1] == closeToOpen[char]:
					stack.pop()
				else:
					return False
			else:
				stack.append(char)
		return True if not stack else False
	'''

# Ex 1:
assert Solution().isValid(s = "()") == True

# Ex 2:
assert Solution().isValid(s = "()[]{}") == True

# Ex 3:
assert Solution().isValid(s = "(]") == False

# Test case 4:
assert Solution().isValid(s = "([{}])") == True

# Test case 5:
assert Solution().isValid(s = "([)]") == False

# Test case 6:
assert Solution().isValid(s = "(") == False

# Test case 7:
assert Solution().isValid(s = ")(") == False

# Test case 8:
assert Solution().isValid(s = "({[") == False

# Test case 9:
assert Solution().isValid(s = "[])") == False

# Test case 10:
assert Solution().isValid(s = "([]{})") == True

# Test case 11:
assert Solution().isValid(s = "([]{})([{}][])") == True