#include <bits/stdc++.h>

using namespace std;

// Graphs - Disjoint Set Union (DSU) approach
// T: O((n + m) * α(n)) ≈ O(n + m), M: O(n)
// Where N = # of nodes, M = # of edges, α(n) = Inverse Ackermann function

class DisjointSetUnion {
private:
    vector<int> parents, sizes;
public:
    // Initialize nodes to single sized node graphs
    DisjointSetUnion(int n) : sizes(n, 1) {
        for (int node = 0; node < n; ++node) 
            parents.push_back(node);
    }

    // Recursively find and assign parent of current node
    int find_parent(int v) {
        if (parents[v] == v) 
            return v;
        return find_parent(parents[v]);
    }

    // Attempt to union two components
    bool union_components(int a, int b) {
        a = find_parent(a), b = find_parent(b);
        if (a == b)     // If nodes are already in same component
            return false;
        
        if (sizes[a] < sizes[b]) 
            swap(a, b);     // Union by size optimization
        // Merge smaller component (b) into larger component (a)
        parents[b] = a;
        sizes[a] += sizes[b];
        return true;
    }
};

class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        // Union connected nodes
        DisjointSetUnion dsu(n);
        for (vector<int>& e : edges) 
            dsu.union_components(e[0], e[1]);
        
        unordered_set<int> components;
        for (int node = 0; node < n; ++node) 
            components.insert(dsu.find_parent(node));
        return components.size();
    }
};

int main(void) {
    int n;
    vector<vector<int>> edges;
    int attempt, answer;

    // Example 1:
    n = 5;
    edges = {{0,1},{1,2},{3,4}};
    attempt = Solution().countComponents(n, edges);
    answer = 2;
    assert(attempt == answer);
    // Example 2:
    n = 5;
    edges = {{0,1},{1,2},{2,3},{3,4}};
    attempt = Solution().countComponents(n, edges);
    answer = 1;
    assert(attempt == answer);
    return 0;
}