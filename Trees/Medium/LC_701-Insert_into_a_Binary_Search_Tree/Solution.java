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
    // Iterative approach
    // T: O(log n) | O(h), M: O(1)
    // Where n is num of nodes, and h is height of a resonably balanced tree
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null)
            return new TreeNode(val);
        
        // Binary Search for insert null position
        TreeNode prev = root, curr = root;
        while (curr != null) {
            prev = curr;
            if (curr.val > val)
                curr = curr.left;
            else
                curr = curr.right;
        }

        // Connect previous node to the new position
        if (prev.val > val)
            prev.left = new TreeNode(val);
        else
            prev.right = new TreeNode(val);

        return root;
    }

    /*
    // Recursive approach
    // T & M: O(log n) | O(h)
    // Where n is num of nodes, and h is height of a resonably balanced tree
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null)
            return new TreeNode(val);

        // Recursively search for null position, then connect previous node to new node
        if (root.val > val)
            root.left = insertIntoBST(root.left, val);      // decrease current node
        else
            root.right = insertIntoBST(root.right, val);    // increase current node
        
        return root;
    }
    */
}