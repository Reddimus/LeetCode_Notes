'''
LeetCode #937 - Reorder Data in Log Files prompt:

You are given an array of logs. Each log is a space-delimited string of words, where 
the first word is the identifier.

There are two types of logs:
1) Letter-logs: All words (except the identifier) consist of lowercase English letters.
2) Digit-logs: All words (except the identifier) consist of digits.

Reorder these logs so that:
- The letter-logs come before all digit-logs.
- The letter-logs are sorted lexicographically by their contents. If their contents 
are the same, then sort them lexicographically by their identifiers.
- The digit-logs maintain their relative ordering.
- Return the final order of the logs.

Example 1:
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

Example 2:
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

Constraints:
1 <= logs.length <= 100
3 <= logs[i].length <= 100
All the tokens of logs[i] are separated by a single space.
logs[i] is guaranteed to have an identifier and at least one word after the identifier.
'''

class Solution:
	# Time complexity: 	O(n + k log k), where n is len of logs arr and k is len of letter logs
	# Space complexity: O(1), returns letter + digit
	def reorderLogFiles(self, logs: list[str]) -> list[str]:
		letter = []
		digit = []
		for log in logs:
			if log.split()[1].isdigit(): 	# check 1st content
				digit.append(log)
			else:
				letter.append(log)
		# sort by suffix [1:], if suffix is tie sort by identifier [0]
		letter.sort(key = lambda x: (x.split()[1:], x.split()[0]))
		return letter + digit 	# combine arrs

	# # Time complexity: 	O(n + k log k), where n is len of logs arr and k is len of letter logs
	# # Space complexity: O(1), returns letter + digit
	# def reorderLogFiles(self, logs: list[str]) -> list[str]:
	# 	letter = []
	# 	digit = []
	# 	for log in logs:
	# 		# iterate string until we find start of 1st content
	# 		char = ""
	# 		idx_0 = 0
	# 		while char != " ":	# ignore while loop in time complexity bc len of content is constant
	# 			char = log[idx_0]
	# 			idx_0 += 1
	# 		# iterate string until we finish end of 1st content
	# 		idx_1 = 0 + idx_0
	# 		char = ""
	# 		while (char != " ") and (idx_1 != len(log)):
	# 			char = log[idx_1]
	# 			idx_1 += 1
	# 		content = log[idx_0:idx_1 - 1]

	# 		if content.isdigit():
	# 			digit.append(log)
	# 		else:
	# 			letter.append(log)
	# 	# sort by suffix [1:], if suffix is tie sort by identifier [0]
	# 	letter.sort(key = lambda x: (x.split()[1:], x.split()[0]))
	# 	return letter + digit

	def testcase(self, logs: list[str], exp: list[str]) -> bool:
		ex = self.reorderLogFiles(logs = logs)
		assert ex == exp, f'Expected {exp}, but got {ex}'

# Ex 1
Solution().testcase(logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"], exp = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"])

# Ex 2
Solution().testcase(logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"], exp = ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])