'''
LeetCode #21 - Merge Two Sorted Lists Prompt:

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made 
by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
	# Time complexity: 	O(2n)
	# Space complexity: O(1)
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		# can evade edge cases where linked list(s) are []
		dummy = ListNode()
		tail = dummy

		while list1 and list2:
			if list1.val < list2.val:
				tail.next = list1
				list1 = list1.next
			else:
				tail.next = list2
				list2 = list2.next
			tail = tail.next
		# link remaining list(s) to prev
		if list1:
			tail.next = list1
		elif list2:
			tail.next = list2
		return dummy.next

	'''
	# Time complexity: 	O(2n)
	# Space complexity: O(1)
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		if (not list1) and (list2):
			return list2
		elif (list1) and (not list2):
			return list1
		elif not list1 and not list2:
			return None

		curr1, curr2 = list1, list2
		# store minimum num of the 2 list into head and iterate the num chosen
		if curr1.val <= curr2.val:
			head = curr1
			curr1 = curr1.next
		else:
			head = curr2
			curr2 = curr2.next
		prev = head

		while curr1 and curr2:
			# point previous chosen num to next smallest number in list1 or list2
			if curr1.val < curr2.val:
				temp = curr1
				curr1 = curr1.next
			else:
				temp = curr2
				curr2 = curr2.next
			prev.next = temp
			prev = prev.next
		# Store last remaining num
		if curr1 != None:
			prev.next = curr1
		else:
			prev.next = curr2
		return head
	'''

def test_case(list1: Optional[ListNode], list2: Optional[ListNode], expected_out: list[int]) -> Optional[ListNode]:
	result = []
	print("Original Linked List 1: [", end = "")
	curr = list1
	while curr:
		print(curr.val, end=", ")
		curr = curr.next
	print("]")

	print("Original Linked List 2: [", end = "")
	curr = list2
	while curr:
		print(curr.val, end=", ")
		curr = curr.next
	print("]")

	curr = Solution().mergeTwoLists(list1, list2)
	print("Merged Linked List: [", end = "")
	while curr:
		result.append(curr.val)
		print(curr.val, end=", ")
		curr = curr.next
	print("]\n")

	assert result == expected_out

# Ex 1:
print("Ex 1:")
node4 = ListNode(4)
node2 = ListNode(2, node4)
node1 = ListNode(1, node2)
list1 = node1
node4 = ListNode(4)
node3 = ListNode(3, node4)
node1 = ListNode(1, node3)
list2 = node1
test_case(list1, list2, [1, 1, 2, 3, 4, 4])

# Ex 2:
print("Ex 2:")
list1 = None
list2 = None
test_case(list1, list2, [])

# Ex 3:
print("Ex 3:")
list1 = None
node0 = ListNode(0)
list2 = node0
test_case(list1, list2, [0])
