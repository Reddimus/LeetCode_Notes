from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left = None, right = None) -> None:
        self.val = val
        self.left, self.right = left, right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        return root


def treeToList(root: Optional[TreeNode]) -> list:
    if not root:
        return []
    
    tree_list = [None]  # Start with a dummy value at index 0
    queue = deque([(root, 1)])
    
    while queue:
        node, index = queue.popleft()
        
        # Extend list size if necessary
        if index >= len(tree_list):
            tree_list.extend([None] * (index - len(tree_list) + 1))
        
        tree_list[index] = node.val
        
        if node.left:
            queue.append((node.left, index * 2))
        if node.right:
            queue.append((node.right, index * 2 + 1))
    
    return tree_list[1:]  # Remove the dummy value at index 0

sol = Solution()

# Ex 1
root = TreeNode(val=4, left=(TreeNode(val=2, left=TreeNode(1), right=TreeNode(3))), right=TreeNode(7))
attempt = sol.insertIntoBST(root, 5)
ans = [4,2,7,1,3,5]
ans2 = [5,2,7,1,3,None,None,None,None,None,None,None,4]
assert treeToList(attempt) == ans or treeToList(attempt) == ans2, f'Expected {ans} or {ans2}, but got {treeToList(attempt)}'
# Ex 2
root = TreeNode(val=40, left=(TreeNode(val=20, left=TreeNode(10), right=TreeNode(30))), right=TreeNode(60, left=TreeNode(50), right=TreeNode(70)))
attempt = sol.insertIntoBST(root, 25)
ans = [40,20,60,10,30,50,70, None, None, 25]
assert treeToList(attempt) == ans, f'Expected {ans}, but got {treeToList(attempt)}'
# Ex 3
root = TreeNode(val=4, left=(TreeNode(val=2, left=TreeNode(1), right=TreeNode(3))), right=TreeNode(7, left=TreeNode(None), right=TreeNode(None)))
attempt = sol.insertIntoBST(root, 5)
ans = [4,2,7,1,3,5]
assert treeToList(attempt) == ans, f'Expected {ans}, but got {treeToList(attempt)}'
