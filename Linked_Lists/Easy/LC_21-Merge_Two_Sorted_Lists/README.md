# LeetCode #21 - Merge Two Sorted Lists

### Difficulty: Easy

https://leetcode.com/problems/merge-two-sorted-lists/

## Problem Description
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

## Example 1
**Input**:  
```
list1 = [1, 2, 4], list2 = [1, 3, 4]
```
**Output**:  
```
[1, 1, 2, 3, 4, 4]
```

## Example 2
**Input**:  
```
list1 = [], list2 = []
```  
**Output**:  
```
[]
```

## Example 3
**Input**:  
```
list1 = [], list2 = [0]
```  
**Output**:  
```
[0]
```

## Constraints
- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in non-decreasing order.

## Hints
- Maintain a dummy node to retrieve the head of the merged list.
- Create a pointer to represent the tail of the new Sorted merged list.
- While iterating through both lists, add the smaller node to the tail of the new list.
- Once you reach the end of one of the lists, add the remaining nodes of the other list to the tail of the new list.

## Solution Explanation

https://github.com/Reddimus/LeetCode_Notes/tree/main/Linked_Lists/Easy/LC_21-Merge_Two_Sorted_Lists

#### Intuition
We can merge two sorted linked lists by iterating through both lists and adding the smaller node to the tail of the new list. Once we reach the end of one of the lists, we can add the remaining nodes of the other list to the tail of the new list. We can maintain a dummy node to retrieve the head of the merged list. 

#### Algorithm
1. Initialize two pointers: `dummy` and `tail`.
2. Iterate through both lists, starting at the `head` node.
3. For each node, add the smaller node to the tail of the new list.
4. Once you reach the end of one of the lists, add the remaining nodes of the other list to the tail of the new list.
5. Return `dummy.next` to retrieve the head of the new Sorted merged list.

#### Complexity Analysis
- **Time Complexity:** `O(n + m)`  
  - Where `n` is the number of nodes in `list1` and `m` is the number of nodes in `list2`.
- **Space Complexity:** `O(1)`
    - We are not using any extra space, so the space complexity is constant.

### Python Solution
```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
        
        # Link remaining list to new Sorted list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next
```

### C++ Solution
```cpp
class Solution {
public:
    ListNode* mergeTwoLists(ListNode *list1, ListNode *list2) {
        ListNode *dummy = new ListNode();
        ListNode *tail = dummy;

        while (list1 && list2) {
            if (list1->val < list2->val) {
                tail->next = list1;
                list1 = list1->next;
            } else {
                tail->next = list2;
                list2 = list2->next;
            }
            tail = tail->next;
        }

        // Link remaining list to new Sorted list
        if (list1)
            tail->next = list1;
        else if (list2)
            tail->next = list2;
        
        return dummy->next;
    }
};
```

### Java Solution
```java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode();
        ListNode tail = dummy;

        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                tail.next = list1;
                list1 = list1.next;
            }
            else {
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }

        // Link remaining list to new Sorted list
        if (list1 != null)
            tail.next = list1;
        else if (list2 != null)
            tail.next = list2;
        
        return dummy.next;
    }
}
```