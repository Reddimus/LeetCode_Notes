'''
LeetCode #701 - Insert Into a Binary Search Tree prompt:

You are given the root node of a binary search tree (BST) and a 
value to insert into the tree. Return the root node of the BST 
after the insertion. It is guaranteed that the new value does 
not exist in the original BST.

Notice that there may exist multiple valid ways for the 
insertion, as long as the tree remains a BST after insertion. 
You can return any of them.

Example 1:
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Example 3:
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]

Constraints:
The number of nodes in the tree will be in the range [0, 10^4].
-10^8 <= Node.val <= 10^8
All the values Node.val are unique.
-10^8 <= val <= 10^8
It's guaranteed that val does not exist in the original BST.
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val: int = 0, left = None, right = None):
		self.val = val
		self.left = left        # left < Parent Node
		self.right = right      # right > Parent Node

class Solution:
	# Time complexity:  O(log n) = O(h)
	# Space complexity: O(log n)
	def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
		if not root:    # if tree doesnt exist insert single node tree
			return TreeNode(val) # & if parent node points to NULL insert node

		if val < root.val:  # iterate left
			root.left = self.insertIntoBST(root.left, val)
		else:           # iterate right
			root.right = self.insertIntoBST(root.right, val)

		return root

# Ex 1:
# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
val = 5
result = Solution().insertIntoBST(root, val)
assert result.val == 4
assert result.left.val == 2
assert result.left.left.val == 1
assert result.left.right.val == 3
assert result.right.val == 7
assert result.right.left.val == 5

# Ex 2:
# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]
root = TreeNode(40)
root.left = TreeNode(20)
root.left.left = TreeNode(10)
root.left.right = TreeNode(30)
root.right = TreeNode(60)
root.right.left = TreeNode(50)
root.right.right = TreeNode(70)
val = 25
result = Solution().insertIntoBST(root, val)
assert result.val == 40
assert result.left.val == 20
assert result.left.left.val == 10
assert result.left.right.val == 30
assert result.right.val == 60
assert result.right.left.val == 50
assert result.right.right.val == 70
assert result.left.right.left.val == 25

# Ex 3:
# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
val = 5
result = Solution().insertIntoBST(root, val)
assert result.val == 4
assert result.left.val == 2
assert result.left.left.val == 1
assert result.left.right.val == 3
assert result.right.val == 7
assert result.right.left.val == 5
