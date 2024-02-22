import java.util.*;

// Graphs - Disjoint Set Union (DSU) approach
// T: O(N * α(N)) ≈ O(N), M: O(N)
// Where N is the number of nodes and α is the Inverse Ackermann function which is roughly O(1) time complexity.

class DisjointSetUnion {
    private int[] parent, size;
    // Initialize nodes to single sized node graphs
    public DisjointSetUnion(int n) {
        size = new int[n];
        Arrays.fill(size, 1);
        parent = new int[n];
        for (int i = 0; i < n; ++i) 
            parent[i] = i;
    }

    // Recursively find and assign parent of current node
    private int findParent(int v) {
        if (parent[v] == v) 
            return v;
        
        parent[v] = findParent(parent[v]);
        return parent[v];
    }

    public boolean unionComponents(int a, int b) {
        a = findParent(a);
        b = findParent(b);
        if (a == b)     // If nodes are already in same component
            return false;

        // Union by size optimization
        if (size[a] < size[b]) {
            int temp = a;
            a = b;
            b = temp;
        }
        // Merge smaller component (b) into larger component (a)
        parent[b] = a;
        size[a] += size[b];
        return true;
    }
}

class Solution {
    int[] findRedundantConnection(int[][] edges) {
        DisjointSetUnion dsu = new DisjointSetUnion(edges.length + 1);
        for (int[] edge : edges) 
            // If node a part of the same component as node b
            if (!dsu.unionComponents(edge[0], edge[1])) 
                return new int[]{edge[0], edge[1]}; // redundant connection

        return new int[]{};
    }
}

class TestCases {
    public static void assertFindRedundantConnection(int[][] edges, int[] answer) {
        int[] attempt = new Solution().findRedundantConnection(edges);
        assert Arrays.equals(attempt, answer) : "Expected " + Arrays.toString(answer) + ", but got " + Arrays.toString(attempt);
    }
    public static void main(String[] args) {
        int[][] edges;
        int[] answer;

        // Example 1
        edges = new int[][]{{1, 2}, {1, 3}, {2, 3}};
        answer = new int[]{2, 3};
        assertFindRedundantConnection(edges, answer);
        // Example 2
        edges = new int[][]{{1, 2}, {2, 3}, {3, 4}, {1, 4}, {1, 5}};
        answer = new int[]{1, 4};
        assertFindRedundantConnection(edges, answer);
    }
}