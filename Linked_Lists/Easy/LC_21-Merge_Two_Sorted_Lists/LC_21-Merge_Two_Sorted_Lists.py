# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val: int = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    # T: O(n), M: O(1), where n is size of biggest linked list input
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
