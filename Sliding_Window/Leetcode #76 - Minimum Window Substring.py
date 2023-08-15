'''
Leetcode #76 - Minimum Window Substring prompt:

Given two strings s and t of lengths m and n respectively, return 
the minimum window substring of s such that every character in t 
(including duplicates) is included in the window. If there is no 
such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', 
and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

class Solution:
	# Time complexity: 	O(n + m)	
	# Space complexity: O(2n) = O(n)
	def minWindow(self, s: str, t: str) -> str:
		if t == "" or len(s) < len(t):
			return ""

		t_count, s_count = {}, {}
		for char in t:
			t_count[char] = 1 + t_count.get(char, 0)

		have, need = 0, len(t_count)	# key chars we need & have in substring/ window
		window_ptrs, len_window = [-1, -1], float("infinity")
		l_ptr = 0
		for r_ptr in range(len(s)):
			r_char = s[r_ptr]
			if r_char in t_count:
				s_count[r_char] = 1 + s_count.get(r_char, 0)
				if s_count[r_char] == t_count[r_char]:
					have += 1

			while have == need:
				# update our window values
				if (r_ptr - l_ptr + 1) < len_window:
					window_ptrs = [l_ptr, r_ptr]
					len_window = r_ptr - l_ptr + 1
				# pop from the left of our window
				if s[l_ptr] in t_count:
					s_count[s[l_ptr]] -= 1
					if s_count[s[l_ptr]] < t_count[s[l_ptr]]:
						have -= 1
				l_ptr += 1
		l_ptr, r_ptr = window_ptrs
		return s[l_ptr : r_ptr + 1] if len_window != float("infinity") else ""

	'''
	# Time complexity: 	O(n + m)	
	# Space complexity: O(n + m)
	def minWindow(self, s: str, t: str) -> str:
		if t == "" or len(s) < len(t):
			return ""

		t_count, window = {}, {}
		for char in t:
			t_count[char] = 1 + t_count.get(char, 0)

		have, need = 0, len(t_count)	# key chars we need & have in substring/ window
		res, resLen = [-1, -1], float("infinity")
		l_ptr = 0
		for r_ptr in range(len(s)):
			r_char = s[r_ptr]
			window[r_char] = 1 + window.get(r_char, 0)
			if r_char in t_count and window[r_char] == t_count[r_char]:
				have += 1

			while have == need:
				# update our result
				if (r_ptr - l_ptr + 1) < resLen:
					res = [l_ptr, r_ptr]
					resLen = r_ptr - l_ptr + 1
				# pop from the left of our window
				window[s[l_ptr]] -= 1
				if s[l_ptr] in t_count and window[s[l_ptr]] < t_count[s[l_ptr]]:
					have -= 1
				l_ptr += 1
		l_ptr, r_ptr = res
		return s[l_ptr : r_ptr + 1] if resLen != float("infinity") else ""
	'''


# Ex 1
assert Solution().minWindow(s = "ADOBECODEBANC", t = "ABC") == "BANC"

# Ex 2
assert Solution().minWindow(s = "a", t = "a") == "a"

# Ex 3
assert Solution().minWindow(s = "a", t = "aa") == ""