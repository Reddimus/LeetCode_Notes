'''
Leetcode #206 - Reverse Linked List prompt:

Given the head of a singly linked list, reverse the list, and return 
the reversed list.

Example 1:
Graph:
1 -> 2 -> 3 -> 4 -> 5
		  |
		  v
5 -> 4 -> 3 -> 2 -> 1
Input: head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

Example 2:
Graph:
1 -> 2
  |
  v
2 -> 1
Input: head = [1, 2]
Output: [2, 1]

Example 3:
Input: head = []
Output: []
 
Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. 
Could you implement both?
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val = 0, next = None):
		self.val, self.next = val, next

class Solution:
	# Iterative solution
	# Time complexity: 	O(n)
	# Space complexity: O(1)
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		prev, curr = None, head

		while curr:
			# curr.next needs to be initialized before curr
			# temp = curr.next
			# curr.next = prev
			# prev = curr
			# curr = temp
			curr.next, prev, curr = prev, curr, curr.next
		return prev

	'''
	# Recursive solution
	# Time complexity: 	O(n)
	# Space complexity: O(n)
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if not head:	# if node doesnt exist
			return None

		newHead = head 	# recursively assign newhead until we reach the tail
		if head.next:	# if curr node points to a next node in the list
			newHead = self.reverseList(head = head.next)
			# assign next node's ptr to the current node, this will reverse the direction of the pointers
			head.next.next = head
		# assign current node's ptr to nothing to remap & reverse the direction of the ptrs later in if statement
		head.next = None
		return newHead
	'''

def test_case(head, expected_out):
    result = []
    print("Original Linked List: [", end = "")
    curr = head
    while curr:
        print(curr.val, end=", ")
        curr = curr.next
    print("]")

    curr = Solution().reverseList(head)
    print("Reversed Linked List: [", end = "")
    while curr:
        result.append(curr.val)
        print(curr.val, end=", ")
        curr = curr.next
    print("]\n")

    assert result == expected_out

# Ex 1:
print("Ex 1:")
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head = node1
test_case(head, [5, 4, 3, 2, 1])

# Ex 2:
print("Ex 2:")
node2 = ListNode(2)
node1 = ListNode(1, node2)
head = node1
test_case(head, [2, 1])

# Ex 3:
print("Ex 3:")
head = []
test_case(head, [])
