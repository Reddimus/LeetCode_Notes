'''
LeetCode #23 - Merge k Sorted Lists prompt:

You are given an array of k linked-lists lists, each linked-list is 
sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5], [1,3,4], [2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 
Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.
'''
from typing import Optional

class ListNode:
	def __init__(self, val: int):
		self.val = val
		self.next = None

class Solution:
	# Time complexity: 	O(n log k), where k = num of linked lists in arr, n = total num of nodes
	# Space complexity: O(1)
	def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
		if not lists or len(lists) == 0:	# if lists is empty
			return None
		# iterate until we have a single sorted list
		while len(lists) > 1:
			mergedLists = []
			for idx in range(0, len(lists), 2): 	# compare two linked lists at a time
				l1 = lists[idx]
				# if second linked list is out of range l2 = None
				l2 = lists[idx + 1] if (idx + 1) < len(lists) else None
				mergedLists.append(self.mergeList(l1, l2))
			lists = mergedLists
		return lists[0]

	# Time complexity: 	O(n)
	# Space complexity: O(1)
	def mergeList(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		dummy = ListNode(0)
		tail = dummy
		# Compare vals and merge
		while l1 and l2:
			if l1.val < l2.val:
				tail.next = l1
				l1 = l1.next
			else:
				tail.next = l2
				l2 = l2.next
			tail = tail.next
		# Check for remaining nums
		if l1:
			tail.next = l1
		elif l2:
			tail.next = l2
		return dummy.next 	# head

class TestCases:
	def arr_to_ll(self, arr: list[int]) -> Optional[ListNode]:
		dummy = ListNode(0)
		curr = dummy
		for val in arr:
			curr.next = ListNode(val)
			curr = curr.next
		return dummy.next # head

	def check_vals(self, attempt: Optional[ListNode], ans: list[int]):
		ans = self.arr_to_ll(ans)
		while attempt and ans: 	# iterate linked lists and check values
			assert attempt.val == ans.val
			attempt, ans = attempt.next, ans.next

s, t = Solution(), TestCases()

# Ex 1:
ex1 = s.mergeKLists(lists = [t.arr_to_ll([1,4,5]), t.arr_to_ll([1,3,4]), t.arr_to_ll([2,6])])
t.check_vals(attempt = ex1, ans = [1, 1, 2, 3, 4, 4, 5, 6])

# Ex 2:
ex2 = s.mergeKLists(lists = [])
t.check_vals(attempt = ex2, ans = [])

# Ex 3:
ex3 = s.mergeKLists(lists = [[]])
t.check_vals(attempt = ex3, ans = [])