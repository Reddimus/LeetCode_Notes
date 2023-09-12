# Leetcode #206 - Reverse Linked List

### Easy

https://leetcode.com/problems/reverse-linked-list/description/

## Problem Statement
Given the `head` of a singly linked list, reverse the list, and return the reversed list.

## Examples

### Example 1
**Graph:**
```plaintext
1 -> 2 -> 3 -> 4 -> 5
  |
  v
5 -> 4 -> 3 -> 2 -> 1
```

**Input:** head = [1, 2, 3, 4, 5]  
**Output:** [5, 4, 3, 2, 1]

### Example 2
**Graph:**
```
1 -> 2  
  |
  v
2 -> 1  
```
**Input:** head = [1, 2]  
**Output:** [2, 1]

### Example 3
**Input:** head = []  
**Output:** []  

## Constraints
- The number of nodes in the list is in the range `[0, 5000]`.  
- `-5000 <= Node.val <= 5000`

## Follow Up
A linked list can be reversed either iteratively or recursively. Could you implement both?


## Hints
- For the recursive solution, assume the rest of the list had already been reversed, now how do I reverse the front part?
- Think about the base case of the recursion. What is the reverse of an empty list? A single node? What should the recursive function do if the list has only two nodes?

## Solution Explanation

https://github.com/Reddimus/LeetCode_Notes/tree/main/Linked_Lists/Easy/LC_206-Reverse_Linked_List

### Approach: Iterative
#### Intuition
We can reverse a linked list by changing the direction of the pointers. We can do this by iterating through the list using 2 variables the current node & previous dummy node and changing the direction of the pointers as we go.

#### Algorithm
1. Initialize three pointers: `prev`, `curr`, and `next`.
2. Iterate through the list, starting at the `head` node.
3. For each node, set `next` to the next node in the list.
4. Set the `next` pointer of the current node to the previous node.
5. Set the `prev` pointer to the current node.
6. Set the `curr` pointer to the next node.
7. Repeat steps 3-6 until `curr` is `None`.
8. Return `prev`.

#### Complexity Analysis
- **Time Complexity:** `O(n)`, where `n` is the number of nodes in the list.
- **Space Complexity:** `O(1)`.
  - We only use three pointers, so the space complexity is constant.

### Python Solution
```python
class Solution:
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		prev, curr = None, head
		while curr:
			curr.next, prev, curr = prev, curr, curr.next
		return prev
```

### C++ Solution
```cpp
class Solution {
public:
	ListNode* reverseList(ListNode* head) {
		ListNode *prev = NULL;
		ListNode *curr = head;

		while (curr) {
			ListNode *temp = curr->next;
			curr->next = prev;
			prev = curr;
			curr = temp;
		}
		return prev;
	}
};
```

### Java Solution
```java
class Solution {
	public ListNode reverseList(ListNode head) {
		ListNode prev = null, curr = head;

		while (curr != null) {
			ListNode temp = curr.next;
			curr.next = prev;
			prev = curr;
			curr = temp;
		}

		return prev;
	}
}
```

### Approach: Recursive
#### Intuition
We can reverse a linked list by changing the direction of the pointers after recursively calling the function to the end of the orignal Linked List.

#### Algorithm
1. If the `head` is `None` or the `head` is the last node in the list, return the `head`.
2. Recursively call the function on the next node in the list.
3. Set the `next` pointer of the next node to the current node.
4. Set the `next` pointer of the current node to `None`.
5. Return the next node.

#### Complexity Analysis
- **Time Complexity:** `O(n)`, where `n` is the number of nodes in the list.
- **Space Complexity:** `O(n)`.
  - The space complexity is `O(n)` because we are using `n` stack frames for the recursive calls.

### Python Solution
```python
class Solution:
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if not head:
			return None

		newHead = head
		if head.next:
			newHead = self.reverseList(head = head.next)
			head.next.next = head
		head.next = None

		return newHead
```

### C++ Solution
```cpp
class Solution {
public:
	ListNode* reverseList(ListNode* head) {
		if (!head || !head->next)
			return head;

		ListNode *newHead = reverseList(head->next);
		head->next->next = head;
		head->next = NULL;

		return newHead;
	}
};
```

### Java Solution
```java
class Solution {
	public ListNode reverseList(ListNode head) {
		if (head == null || head.next == null)
			return head;
		
		ListNode newHead = reverseList(head.next);
		head.next.next = head;
		head.next = null;
		
		return newHead;
	}
}
```