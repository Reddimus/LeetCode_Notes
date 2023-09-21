// Binary Search Tree Data Structure
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode() {}
    TreeNode(int x) { this.val = x; }
    TreeNode(int x, TreeNode left, TreeNode right) {
        this.val = x;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    // Recursive approach
    // T: O(log n) | O(h), M: O(n)
    // Where n is num of nodes, and h is height of resonably balanced tree
    TreeNode searchBST(TreeNode root, int val) {
        if (root == null)
            return null;
        
        if (root.val < val) 
            return searchBST(root.right, val);
        else if (root.val > val)
            return searchBST(root.left, val);
        return root;
    }

    /*
    // Iterative approach
    // T: O(log n) | O(h), M: O(1)
    // Where n is num of nodes, and h is height of resonably balanced tree
    TreeNode searchBST(TreeNode root, int val) {
        while (root != null) {
            if (root.val < val) 
                root = root.right;
            else if (root.val > val)
                root = root.left;
            else
                return root;
        }
        return null;
    }
    */
}

class TestCases {
    public static void main(String[] args) {
        // In terminal:
        // $ javac Solution.java
        // $ java -ea TestCases
        Solution sol = new Solution();
        TreeNode root, attempt;

        // Ex1
        root = new TreeNode(4, new TreeNode(2, new TreeNode(1), new TreeNode(3)), new TreeNode(7));
        attempt = sol.searchBST(root, 2);
        assert attempt.val == 2 : "Expected 2, but got " + attempt.val;
        // Ex2
        root = new TreeNode(4, new TreeNode(2, new TreeNode(1), new TreeNode(3)), new TreeNode(7));
        attempt = sol.searchBST(root, 5);
        assert attempt == null : "Expected null, but got " + attempt;
    }
}