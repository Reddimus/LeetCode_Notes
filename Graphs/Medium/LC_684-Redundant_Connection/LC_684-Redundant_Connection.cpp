#include <bits/stdc++.h>

using namespace std;

// Graphs - Disjoint Set Union (DSU) approach
// T: O(N * α(N)) ≈ O(N), M: O(N)
// Where N is the number of nodes and α is the Inverse Ackermann function which is roughly O(1) time complexity.

class DisjointSetUnion {
private:
    vector<int> parent, size;
public:
    // Initialize nodes to single sized node graphs
    DisjointSetUnion(int n) : size(n, 1) {
        for (int node = 0; node < n; ++node) 
            parent.push_back(node);
    }

    // Recursively find and assign parent of current node
    int find_parent(int v) {
        if (parent[v] == v) 
            return v;
        // Path compression optimization
        parent[v] = find_parent(parent[v]);
        return parent[v];
    }

    // Attempt to union two components
    bool union_components(int a, int b) {
        a = find_parent(a), b = find_parent(b);
        if (a == b)     // If nodes are already in same component
            return false;
        
        if (size[a] < size[b])
            swap(a, b);     // Union by size optimization
        // Merge smaller component (b) into larger component (a)
        parent[b] = a;
        size[a] += size[b];
        return true;
    }
};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        DisjointSetUnion dsu(edges.size() + 1);
        for (const vector<int>& e : edges) 
            // If node a part of the same component as node b
            if (!dsu.union_components(e[0], e[1])) 
                return {e[0], e[1]};  // redundant connection
        return {};
    }
};

int main(void) {
    vector<int> attempt, answer;
    vector<vector<int>> edges;

    // Example 1:
    edges = {{1,2}, {1,3}, {2,3}};
    attempt = Solution().findRedundantConnection(edges);
    answer = {2,3};
    assert(attempt == answer);
    // Example 2:
    edges = {{1,2}, {2,3}, {3,4}, {1,4}, {1,5}};
    attempt = Solution().findRedundantConnection(edges);
    answer = {1,4};
    assert(attempt == answer);
    return 0;
}