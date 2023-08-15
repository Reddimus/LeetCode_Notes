'''
LeetCode #707 - Design Linked List prompt:

Design your implementation of the linked list. You can choose to use a singly or doubly 
linked list.

A node in a singly linked list should have two attributes: val and next. val is the value of 
the current node, and next is a pointer/reference to the next node.

If you want to use the doubly linked list, you will need one more attribute prev to indicate 
the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.

int get(int index) Get the value of the indexth node in the linked list. If the index is 
invalid, return -1.

void addAtHead(int val) Add a node of value val before the first element of the linked list. 
After the insertion, the new node will be the first node of the linked list.

void addAtTail(int val) Append a node of value val as the last element of the linked list.

void addAtIndex(int index, int val) Add a node of value val before the indexth node in the 
linked list. If index equals the length of the linked list, the node will be appended to the 
end of the linked list. If index is greater than the length, the node will not be inserted.

void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]

Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3


Constraints:
0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
'''

class ListNode:
    def __init__ (self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    # Time and space complexity: O(n)
    def __init__(self):     # initialize r & l dummy values for edge cases
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        curr = self.left.next
        # iterate through linked list until index reached
        while curr and index > 0:
            curr = curr.next
            index -= 1
        # we do not want curr val to be out of bounds
        if curr and curr != self.right and index == 0:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        left_neighbor, node, right_neighbor = self.left, ListNode(val), self.left.next
        # left_nighbor = left dummy,    node = new head,    right_neighbor = prev head
        left_neighbor.next = node
        node.prev = left_neighbor
        node.next = right_neighbor
        right_neighbor.prev = node

    def addAtTail(self, val: int) -> None:
        left_neighbor, node, right_neighbor = self.right.prev, ListNode(val), self.right
        # left_nighbor = prev tail,    node = new tail,    right_neighbor = right dummy
        left_neighbor.next = node
        node.prev = left_neighbor
        node.next = right_neighbor
        right_neighbor.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        # iterate through linked list until index reached
        while curr and index > 0:
            curr = curr.next
            index -= 1
        # we do not want curr to be out of bounds, however we can add one index where right can be
        if curr and index == 0:
            left_neighbor, node, right_neighbor = curr.prev, ListNode(val), curr
            # left_nighbor = prev curr,    node = new val,    right_neighbor = curr
            left_neighbor.next = node
            node.prev = left_neighbor
            node.next = right_neighbor
            right_neighbor.prev = node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        # iterate through linked list until index reached
        while curr and index > 0:
            curr = curr.next
            index -= 1
        # we do not want curr to be out of bounds
        if curr and curr != self.right and index == 0:
            left_neighbor, right_neighbor = curr.prev, curr.next
            # left_nighbor = prev curr,    node = new val,    right_neighbor = curr
            # curr.prev = None 	# Garbage collection will take care of a node with no pointers
            # curr.next = None
            left_neighbor.next = right_neighbor
            right_neighbor.prev = left_neighbor
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# Test case 1
linked_list = MyLinkedList()
linked_list.addAtHead(1)
linked_list.addAtTail(3)
linked_list.addAtIndex(1, 2)
assert linked_list.get(1) == 2
linked_list.deleteAtIndex(1)
assert linked_list.get(1) == 3

# Test case 2
linked_list = MyLinkedList()
linked_list.addAtHead(1)
linked_list.addAtTail(3)
linked_list.addAtIndex(1, 2)
linked_list.addAtIndex(2, 4)
linked_list.addAtIndex(2, 5)
assert linked_list.get(1) == 2
assert linked_list.get(2) == 5
assert linked_list.get(3) == 4
linked_list.deleteAtIndex(1)
assert linked_list.get(1) == 5
assert linked_list.get(2) == 4

# Test case 3
linked_list = MyLinkedList()
linked_list.addAtHead(1)
linked_list.addAtTail(3)
linked_list.addAtIndex(1, 2)
linked_list.addAtIndex(2, 4)
linked_list.addAtIndex(2, 5)
linked_list.addAtIndex(0, 0)
assert linked_list.get(0) == 0
linked_list.deleteAtIndex(0)
assert linked_list.get(0) == 1