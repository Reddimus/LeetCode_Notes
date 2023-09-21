from typing import Optional

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
            if root.val < val:
                root = root.right
            elif root.val > val:
                root = root.left
            else:
                return root
        return None

    '''
    # Recursive approach
    # T: O(log n) | O(h), M: O(1)
    # Where n is num of nodes, and h is height of resonably balanced tree
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        return root
    '''

sol = Solution()

# Ex 1
root = TreeNode(4, left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)), right=TreeNode(7))
answer = root.left
attempt = sol.searchBST(root, 2)
assert attempt == answer, f'Expected 2 at {answer}, but got {attempt.val} at {attempt}'

# Ex 2
root = TreeNode(4, left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)), right=TreeNode(7))
attempt = sol.searchBST(root, 5)
assert attempt == None, f'Expected NULL, but got {attempt.val}'
