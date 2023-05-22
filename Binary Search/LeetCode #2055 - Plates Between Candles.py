'''
There is a long table with a line of plates and candles arranged on top of it. You 
are given a 0-indexed string s consisting of characters '*' and '|' only, where a 
'*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] 
denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the 
number of plates between candles that are in the substring. A plate is considered between 
candles if there is at least one candle to its left and at least one candle to its right 
in the substring.

- For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The 
number of plates between candles in this substring is 2, as each of the two plates has 
at least one candle in the substring to its left and right.

Return an integer array answer where answer[i] is the answer to the ith query.

Example 1:
Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- queries[0] has two plates between candles.
- queries[1] has three plates between candles.

Example 2:
Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
Output: [9,0,0,0,0]
Explanation:
- queries[0] has nine plates between candles.
- The other queries have zero plates between candles.

Constraints:
3 <= s.length <= 10^5
s consists of '*' and '|' characters.
1 <= queries.length <= 10^5
queries[i].length == 2
0 <= lefti <= righti < s.length
'''

class Solution:
	# Time complexity:  O(n + q * log m), where n is size of s str & m is num of cndls in s
	# Space complexity: O(m)
	def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
		# track location of candles in s string
		cndl_idxs = []
		for idx, char in enumerate(s):
			if char == "|":
				cndl_idxs.append(idx)
		# Iterate through each query
		plates = []
		for query in queries:
			l_que, r_que = query    # store substring idxs into l_que & r_que ptrs
			# Find the candles idxs inside the substring
			l_cndl = self.bin_search(arr = cndl_idxs, target = l_que, left = True)
			r_cndl = self.bin_search(arr = cndl_idxs, target = r_que, left = False)
			# Calculate: plates in between first candle & right candle - all candles
			if l_cndl < r_cndl:
				plts_cndls = cndl_idxs[r_cndl] - cndl_idxs[l_cndl]
				all_cndls = r_cndl - l_cndl
				plates.append(plts_cndls - all_cndls)
			else:
				plates.append(0)
		return plates

	# Time complexity:  O(log m)
	# Space complexity: O(1)
	def bin_search(self, arr: list[int], target: int, left: bool) -> int:
		l_ptr, r_ptr = 0, len(arr) - 1
		while l_ptr <= r_ptr:
			mid = l_ptr + ((r_ptr - l_ptr) // 2)    # left + (half dist); avoid overflow
			if arr[mid] < target:
				l_ptr = mid + 1
			elif arr[mid] > target:
				r_ptr = mid - 1
			else:   # target found
				return mid
		# if target is not in arr
		if left:    # we are looking for first candle idx
			return l_ptr    # return idx closest to starting substring idx
		else:       # we are looking for last candle idx
			return r_ptr    # return idx closest to ending substring idx


	# # Time complexity: 	O(m * n), where m is the size of queries and n is the size of s
	# # Space complexity: O(1)
	# def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
	# 	plates_que = []
	# 	for query in queries:
	# 		start, end = query
	# 		plates = tmp_plt = 0
	# 		cndle_cnt = 0
	# 		for item in s[start:end + 1]:  # iterate through candle or plate in query substring
	# 			if item == '|':  # candle
	# 				cndle_cnt += 1
	# 				if cndle_cnt > 1:  # we have at least two candles, so we can count the plates
	# 					plates += tmp_plt
	# 					tmp_plt = 0  # reset sub plates between candles
	# 			elif item == '*' and cndle_cnt > 0:  # if item is a plate after any candle, count plate temporarily
	# 				tmp_plt += 1
	# 		plates_que.append(plates)
	# 	return plates_que


	def test_platesBetweenCandles(self, s: str, queries: list[list[int]], exp: list[int]) -> bool:
		ex = self.platesBetweenCandles(s = s, queries = queries)
		assert ex == exp, f'Expected {exp}, but got {ex}'

# Ex 1:
Solution().test_platesBetweenCandles(s = "**|**|***|", queries = [[2,5],[5,9]], exp = [2,3])

# Ex 2:
Solution().test_platesBetweenCandles(s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]], exp = [9,0,0,0,0])

# Ex 3:
Solution().test_platesBetweenCandles(s = "*|*||||**|||||||*||*||*||**|*|*||*", queries = [[2,33],[2,32],[3,31],[0,33],[1,24],[3,20],[7,11],[5,32],[2,31],[5,31],[0,31],[3,28],[4,33],[6,29],[2,30],[2,28],[1,30],[1,33],[4,32],[5,30],[4,23],[0,30],[3,10],[5,28],[0,28],[4,28],[3,33],[0,27]], exp = [9,9,9,10,6,4,0,9,9,9,10,7,9,8,8,7,9,10,9,8,5,9,2,7,8,7,9,8])