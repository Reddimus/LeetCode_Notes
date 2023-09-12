# Leetcode #206 - Reverse Linked List

### Easy

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
