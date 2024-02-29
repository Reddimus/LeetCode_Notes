import java.util.*;

// Graphs - Disjoint Set Union (DSU) approach
// T: O((n + m) * α(n)) ≈ O(n + m), M: O(n)
// Where N = # of nodes, M = # of edges, α(n) = Inverse Ackermann function

class DisjointSetUnion {
    private int[] parents, sizes;
    // Initialize nodes to single sized node graphs
    public DisjointSetUnion(int n) {
        sizes = new int[n];
        Arrays.fill(sizes, 1);
        parents = new int[n];
        for (int node = 0; node < n; ++node) 
            parents[node] = node;
    }

    // Recursively find and assign parent of current node
    public int findParent(int v) {
        if (parents[v] == v) 
            return v;
        return findParent(parents[v]);
    }

    // Attempt to union two components
    public boolean unionComponents(int a, int b) {
        a = findParent(a);
        b = findParent(b);
        if (a == b)     // If nodes are already in same component
            return false;
        // Union by size optimization
        if (sizes[a] < sizes[b]) {
            int temp = a;
            a = b;
            b = temp;
        }
        // Merge smaller component (b) into larger component (a)
        parents[b] = a;
        sizes[a] += sizes[b];
        return true;
    }
}

class Solution {
    int countComponents(int n, int[][] edges) {
        // Union connected nodes
        DisjointSetUnion dsu = new DisjointSetUnion(n);
        for (int[] e : edges) 
            dsu.unionComponents(e[0], e[1]);
        
        HashSet<Integer> components = new HashSet<>();
        for (int node = 0; node < n; ++node) 
            components.add(dsu.findParent(node));
        return components.size();
    }
}

class TestCases {
    public static void main(String[] args) {
        // In terminal:
        // Compile:     "javac Solution.java"
        // Test cases:  "java -ea TestCases"
        int n;
        int[][] edges;
        int attempt, answer;

        // Example 1:
        n = 5;
        edges = new int[][]{{0,1},{1,2},{3,4}};
        attempt = new Solution().countComponents(n, edges);
        answer = 2;
        assert attempt == answer : "Expected " + answer + " but got " + attempt;
        // Example 2:
        n = 5;
        edges = new int[][]{{0,1},{1,2},{2,3},{3,4}};
        attempt = new Solution().countComponents(n, edges);
        answer = 1;
        assert attempt == answer : "Expected " + answer + " but got " + attempt;
    }
}