from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Iterative approach
    # T: O(log n) | O(h), M: O(1)
    # Where n is num of nodes, and h is height of resonably balanced tree
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if val > root.val:
                root = root.right   # increase curr node value
            elif val < root.val:
                root = root.left    # decrease curr node value
            else:                # Found value
                return root
        return None
    
    '''
    # Recursive approach
    # T & M: O(log n) | O(h)
    # Where n is num of nodes, and h is height of resonably balanced tree
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Search for value
        if root.val > val:
            return self.searchBST(root.left, val)   # decrease curr val
        elif root.val < val:
            return self.searchBST(root.right, val)  # increase curr val

        return root # Found value
    '''