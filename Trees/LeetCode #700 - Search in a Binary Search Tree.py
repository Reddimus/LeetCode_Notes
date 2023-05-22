'''
LeetCode #700 - Search in a Binary Search Tree prompt:

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the 
subtree rooted with that node. If such a node does not exist, return null.

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:
The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 10^7
root is a binary search tree.
1 <= val <= 10^7
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val: int = 0, left = None, right = None):
		self.val = val
		self.left = left	# left child  < parent node
		self.right = right 	# right child > parent node

class Solution:
	# n = total nodes, h = height of tree
	# Time complexity: 	O(log n) = O(h), in each iter, the method eliminates half of the remaining nodes.
	# Wirst case time complexity: O(n), if Binary Search Tree (BST) is not balanced and continuously checks one side
	# Space complexity: O(log n), due to recursive calls in the call stack
	def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
		if not root:
			return None
		if root.val > val:
			return self.searchBST(root.left, val)
		elif root.val < val:
			return self.searchBST(root.right, val)
		else:	# root.val == val
			return root


def listToTree(arr: list[int], i: int = 0) -> Optional[TreeNode]:
	if i >= len(arr) or arr[i] is None:
		return None
	return TreeNode(arr[i], listToTree(arr, 2 * i + 1), listToTree(arr, 2 * i + 2))

# Example 1: [4,2,7,1,3], val = 2
root, val = listToTree([4, 2, 7, 1, 3]), 2
assert Solution().searchBST(root, val).val == 2
assert Solution().searchBST(root, val).left.val == 1
assert Solution().searchBST(root, val).right.val == 3

# Example 2: [4,2,7,1,3], val = 5
root, val = listToTree([4, 2, 7, 1, 3]), 5
assert Solution().searchBST(root, val) == None
