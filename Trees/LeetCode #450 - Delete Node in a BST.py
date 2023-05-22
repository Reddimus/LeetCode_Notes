'''
LeetCode #450 - Delete Node in a BST prompt:

Given a root node reference of a BST and a key, delete the node with the given 
key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
1. Search for a node to remove.
2. If the node is found, delete the node.


Example 1:
Input: root = [5,3,6,2,4,null,7], key = 3
			5
	3				6
2		4 		Nul		7

Output: [5,4,6,2,null,null,7]
			5
	4				6
2		nul 	nul 	7

Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:
Input: root = [5,3,6,2,4,null,7], key = 0
			5
	3				6
2		4 		nul 	7

Output: [5,3,6,2,4,null,7]
			5
	3				6
2		4 		nul 	7

Explanation: The tree does not contain a node with value = 0.

Example 3:
Input: root = [], key = 0
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
Each node has a unique value.
root is a valid binary search tree.
-10^5 <= key <= 10^5

Follow up: Could you solve it with time complexity O(height of tree)?
'''
from typing import Optional

class TreeNode:
	def __init__(self, val: int = 0, left = None, right = None):
		self.val = val
		self.left = left 	# left 	< parent node
		self.right = right 	# right > parent node

class Solution:
	# Time complexity: 	O(2 log n) = O(2h) = O(log n) = O(h)
	# Space complexity: O(2 log n) = O(2h) = O(log n) = O(h)
	# Worst case we need to find key val & find minNode in subtree O(h), then remove minNode O(h)
	def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
		if not root:	# if tree or subtree is empty there is nothing to delete
			return None

		if key < root.val: 		# iterate left
			root.left = self.deleteNode(root.left, key)
		elif key > root.val: 	# iterate right
			root.right = self.deleteNode(root.right, key)
		else:	# key value found
			if not root.right:   # parent node has only left child
				return root.left
			elif not root.left: # parent node has only right child
				return root.right
			# parent node has 2 children
			minNode = self.minBST(root.right) 	# store minNode in right child subtree
			root.val = minNode.val 				# swap minNode with key node
			root.right = self.deleteNode(root.right, minNode.val)
		return root

	def minBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		curr = root
		while curr and curr.left:
			curr = curr.left
		return curr # return min node


def to_list(root: Optional[TreeNode]):
	if not root:
		return None
	return (root.val, to_list(root.left), to_list(root.right))

# Ex 1:
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
result = Solution().deleteNode(root, 3)
assert result.val == 5
assert result.left.val == 4
assert result.left.left.val == 2
assert result.right.val == 6
assert result.right.right.val == 7

# Example 2:
# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
result = Solution().deleteNode(root, 0)
assert result.val == 5
assert result.left.val == 3
assert result.left.left.val == 2
assert result.left.right.val == 4
assert result.right.val == 6
assert result.right.right.val == 7

# Example 3:
# Input: root = [], key = 0
# Output: []
root = None
result = Solution().deleteNode(root, 0)
assert result == None
