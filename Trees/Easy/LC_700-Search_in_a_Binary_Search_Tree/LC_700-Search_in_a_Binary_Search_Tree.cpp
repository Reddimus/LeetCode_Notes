// #include <bits/stdc++.h>
#include <iostream>
#include <cassert>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    // Iterative approach
    // T: O(log n) | O(h), M: O(1)
    // Where n is num of nodes, and h is height of resonably balanced tree
    TreeNode *searchBST(TreeNode *root, int val) {
        while (root) {
            if (root->val < val) 
                root = root->right;
            else if (root->val > val)
                root = root->left;
            else
                return root;
        }
        return NULL;
    }

    /*
    // Recursive approach
    // T: O(log n) | O(h), M: O(n)
    // Where n is num of nodes, and h is height of resonably balanced tree
    TreeNode *searchBST(TreeNode *root, int val) {
        if (!root)
            return NULL;
        
        if (root->val < val) 
            return searchBST(root->right, val);
        else if (root->val > val) 
            return searchBST(root->left, val);
        return root;
    }
    */
};

int main() {
    TreeNode root, *attempt;
    // Ex 1
    root = TreeNode(4, new TreeNode(2, new TreeNode(1), new TreeNode(3)), new TreeNode(7));
    attempt = Solution().searchBST(&root, 2);
    assert(attempt->val == 2);
    // Ex 2
    root = TreeNode(4, new TreeNode(2, new TreeNode(1), new TreeNode(3)), new TreeNode(7));
    attempt = Solution().searchBST(&root, 5);
    assert(attempt == NULL);

    return 0;
}
