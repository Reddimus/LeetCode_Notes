from typing import Optional

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val: int = 0, next = None) -> None:
		self.val, self.next = val, next

class Solution:
	# Iterative solution
	# T: O(n), M: O(1), where n is the number of nodes in the linked list
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		prev, curr = None, head
		while curr:
			curr.next, prev, curr = prev, curr, curr.next
		return prev

	'''
	# Recursive solution
	# T & M: O(n), where n is the number of nodes in the linked list
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
