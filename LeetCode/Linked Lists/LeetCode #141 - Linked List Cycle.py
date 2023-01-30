'''
LeetCode #141 - Linked List Cycle prompt:

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again 
by continuously following the next pointer. Internally, pos is used to denote the index of the 
node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node 
(0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''
from typing import Optional

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# Floyd's Tortoise & Hare
	# Time complexity: 	O(n)
	# Space complexity: O(1)
	def hasCycle(self, head: Optional[ListNode]) -> bool:
		slow, fast = head, head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:	# if ptrs meet then there is a cycle
				return True
		return False

	'''
	# Hash table solution
	# Time complexity: 	O(n)
	# Space complexity: O(n)
	def hasCycle(self, head: Optional[ListNode]) -> bool:
		addr_table = set()
		while head:
			if head in addr_table:
				return True
			addr_table.add(head)
			head = head.next
		return False
	'''

def arr_to_linked_list(arr: list[int], pos: int) -> Optional[ListNode]:
	dummy = ListNode(0)
	curr = dummy
	nodes = {}
	for idx, val in enumerate(arr):
		curr.next = ListNode(val)
		nodes[idx] = curr.next
		curr = curr.next
	if pos != -1:
		curr.next = nodes[pos] # grab tail and point it to pos
	return dummy.next # return head

# Ex 1:
assert Solution().hasCycle(arr_to_linked_list(arr = [3,2,0,-4], pos = 1)) == True

# Ex 2:
assert Solution().hasCycle(arr_to_linked_list(arr = [1,2], pos = 0)) == True

# Ex 3:
assert Solution().hasCycle(arr_to_linked_list(arr = [1], pos = -1)) == False