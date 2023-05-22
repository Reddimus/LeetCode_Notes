'''
LeetCode #19 - Remove Nth Node from End of List prompt:

Given the head of a linked list, remove the nth node 
from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val: int):
		self.val = val
		self.next = None

class Solution:
	# Time complexity:  O(n)
	# Space complexity: O(1)
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		# len(linked list) >= n
		dummy = ListNode(0)
		dummy.next = head
		# iterate through linked list n times
		left, right = dummy, head   # left will always be left of target node
		while n > 0:
			right = right.next
			n -= 1
		# iterate through remaining times
		while right:	# len(linked list) - n = target
			left, right = left.next, right.next
		# unlink target
		left.next = left.next.next
		return dummy.next

	'''
	# Array solution
	# Time complexity:	O(n)
	# Space complexity: O(n)
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		curr = head
		ll_arr = []
		while curr:
			ll_arr.append(curr)
			curr = curr.next
		target_idx = len(ll_arr) - n
		if target_idx != 0:
			target, prev = ll_arr[target_idx], ll_arr[target_idx - 1]
			prev.next = target.next
			target.next = None
			return head

		return head.next
	'''
class TestCases:
	def arr_to_ll(self, arr: list[int]) -> Optional[ListNode]:
		dummy = ListNode(0)
		curr = dummy
		for val in arr:
			curr.next = ListNode(val)
			curr = curr.next
		return dummy.next 	# return head

	def check_vals(self, attempt: Optional[ListNode], ans: list[int]):
		ans = self.arr_to_ll(ans)
		while attempt and ans:	# iterate and check values
			assert attempt.val == ans.val
			attempt, ans = attempt.next, ans.next

s, test = Solution(), TestCases()
# Ex 1:
ex1 = test.arr_to_ll([1,2,3,4,5])
test.check_vals(attempt = s.removeNthFromEnd(head = ex1, n = 2), ans = [1,2,3,5])

# Ex 2:
ex2 = test.arr_to_ll([1])
test.check_vals(attempt = s.removeNthFromEnd(head = ex2, n = 1), ans = [])

# Ex 3:
ex3 = test.arr_to_ll([1,2])
test.check_vals(attempt = s.removeNthFromEnd(head = ex3, n = 1), ans = [1])
