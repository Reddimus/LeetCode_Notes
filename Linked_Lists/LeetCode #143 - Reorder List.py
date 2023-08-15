'''
LeetCode #143 - Reorder List prompt:

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = 	[1,	2,	3,	4]
Output: 		[1,	4,	2,	3]

Example 2:
Input: head = 	[1,	2,	3,	4,	5]
Output: 		[1,	5,	2,	4,	3]
 
Constraints:

The number of nodes in the list is in the range [1, 5 * 10^4].
1 <= Node.val <= 1000
'''

from typing import Optional

class ListNode:
	def __init__(self, val: int):
		self.val = val
		self.next = None

class Solution:
	# Time complexity: 	O(2n) = O(n)
	# Space complexity: O(1)
	def reorderList(self, head: Optional[ListNode]) -> None:
		# find middle
		slow, fast = head, head.next
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		# reverse second half
		second = slow.next
		prev = slow.next = None 	# assign prev (tail points to NULL) & break first half
		while second:
			tmp = second.next
			second.next = prev
			prev = second
			second = tmp
		second = prev 	# update head for second half

		# merge two halfs
		first = prev
		while second:
			tmp1, tmp2 = first.next, second.next 	# 1 increment ahead
			first.next = second
			second.next = tmp1
			first, second = tmp1, tmp2
	'''
	# array solution
	# Time complexity: 	O(2n) = O(n)
	# Space complexity: O(n)
	def reorderList(self, head: Optional[ListNode]) -> None:
		# store nodes with their order
		ll_arr = []
		while head:
			ll_arr.append(head)
			head = head.next	# iterate through linked list
		# reorder nodes
		l_ptr, r_ptr = 0, len(ll_arr) - 1
		curr = None 	# current node
		while l_ptr <= r_ptr:
			inc_node, dec_node = ll_arr[l_ptr], ll_arr[r_ptr]
			if curr:
				curr.next = inc_node
			inc_node.next = dec_node
			inc_node = inc_node.next
			curr = inc_node
			l_ptr += 1
			r_ptr -= 1
		# Linked List is reordered
		if curr.next:
			curr.next = None # curr points to NULL as it is the tail
		"""
		Do not return anything, modify head in-place instead.
		"""
	'''

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end = " -> ")
        curr = curr.next
    print("None")

# Example 1
print("Example 1: ")
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print("Input: ", end = "")
print_list(head)
s = Solution()
s.reorderList(head)
print("Output: ", end = "")
print_list(head)

# Example 2
print("Example 2: ")
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print("Input: ", end = "")
print_list(head)
s = Solution()
s.reorderList(head)
print("Output: ", end = "")
print_list(head)