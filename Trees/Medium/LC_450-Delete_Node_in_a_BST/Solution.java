
// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    // Recursive approach
    // T & M: O(log n) | O(h)
    // Where n is num of nodes, and h is height of a resonably balanced tree
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null)
            return null;

        // Binary search for desired node
        if (root.val > key) {
            root.left = deleteNode(root.left, key);
        }
        else if (root.val < key) {
            root.right = deleteNode(root.right, key);
        }
        else {
            if (root.left == null)
                return root.right;
            else if (root.right == null)
                return root.left;
            
            // Recursively del & replace the min node of the right subtree
            TreeNode minNode = searchMinNode(root.right);
            root.val = minNode.val;
            root.right = deleteNode(root.right, minNode.val);
        }

        return root;
    }

    private TreeNode searchMinNode(TreeNode curr) {
        while (curr != null && curr.left != null)
            curr = curr.left;
        return curr;
    }

    /*
    // Iterative approach
    // T: O(log n) | O(h), M: O(1)
    // Where n is num of nodes, and h is height of a resonably balanced tree
    public TreeNode deleteNode(TreeNode root, int key) {
        // Find node to be deleted and its parent
        TreeNode parent = null, curr = root;
        while (curr != null && curr.val != key) {
            parent = curr;
            if (curr.val > key)
                curr = curr.left;
            else
                curr = curr.right;
        }

        if (curr == null)   // Node to delete not found
            return root;

        // Case 1: Node with only one child or no child
        if (curr.left == null || curr.right == null) {
            TreeNode child = (curr.left != null) ? curr.left : curr.right;

            // Root is the desired node; del root
            if (parent == null)
                return child;

            if (parent.left == curr)
                parent.left = child;
            else
                parent.right = child;
        }
        // Case 2: Node with two children
        else {
            // Find the minimum valued node in the right subtree
            TreeNode minParent = curr, minNode = curr.right;
            while (minNode != null && minNode.left != null) {
                minParent = minNode;
                minNode = minNode.left;
            }

            // Reconnect minParent to minNode's child or nullptr
            if (minParent != curr)
                minParent.left = minNode.right;
            else
                minParent.right = minNode.right;

            // Replace desired node's val with minNode's val
            curr.val = minNode.val;
        }

        return root;
    }
    */
}

class TestCases {
    public static void main(String[] args) {

    }
}