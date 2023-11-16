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
        parent, node = None, root
        while node and node.val != key:
            parent = node
            if key < node.val:
                node = node.left
            else:
                node = node.right

        if not node:  # Node to delete not found
            return root

        # Case 1: Node with only one child or no child
        if not node.left or not node.right:
            new_node = node.left if node.left else node.right

            # Root is the desired node
            if not parent:  # Deleting the root node
                return new_node

            if parent.left == node:
                parent.left = new_node
            else:
                parent.right = new_node

        # Case 2: Node with two children
        else:
            min_parent, min_node = node, node.right

            # Find the minimum valued node in the right subtree
            while min_node.left:
                min_parent = min_node
                min_node = min_node.left

            # Reconnect min_parent to min_node child or del non-parent min_node
            if min_parent != node:
                min_parent.left = min_node.right
            else:
                min_parent.right = min_node.right

            # Replace node's value with its min_node's value
            node.val = min_node.val

        return root