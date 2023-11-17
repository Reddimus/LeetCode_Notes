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
    # Where n is num of nodes, and h is height of a resonably balanced tree
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Find node to be deleted and its parent
        parent, curr = None, root
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if not curr:  # Node to delete not found
            return root

        # Case 1: Node with only one child or no child
        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right

            # Root is the desired node
            if not parent:  # Deleting the root node
                return child

            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child

        # Case 2: Node with two children
        else:
            # Find the minimum valued node in the right subtree
            min_parent, min_node = curr, curr.right
            while min_node.left:
                min_parent = min_node
                min_node = min_node.left

            # Reconnect min_parent to min_node's child or del non-parent min_node
            if min_parent != curr:
                min_parent.left = min_node.right
            else:
                min_parent.right = min_node.right

            # Replace node's value with its min_node's value
            curr.val = min_node.val

        return root