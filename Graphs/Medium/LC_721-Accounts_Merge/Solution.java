import java.util.*;

// Graphs - Disjoint Set Union (DSU) approach
// T: O(N * E * α(N) + E log E) ≈ O(N * E + E log E), M: O(N + E)
// Where N = # of accounts, E = # of emails, α(N) = Inverse Ackermann function

class DisjointSetUnion {
    private int[] parent, size;
    // Initialize nodes to single sized node graphs
    public DisjointSetUnion(int n) {
        size = new int[n];
        Arrays.fill(size, 1);
        parent = new int[n];
        for (int node = 0; node < n; ++node) 
            parent[node] = node;
    }

    // Recursively find and assign parent of current node
    public int findParent(int v) {
        if (parent[v] == v)
            return v;
        // Path compression optimization
        return findParent(parent[v]);
    }

    // Attempt to union two components
    public boolean unionComponents(int a, int b) {
        a = findParent(a);
        b = findParent(b);
        if (a == b) // If nodes are already in same component
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
    List<List<String>> accountsMerge(List<List<String>> accounts) {
        // Map emails to their respective account index
        final int n = accounts.size();
        DisjointSetUnion dsu = new DisjointSetUnion(n);
        HashMap<String, Integer> accountsMap = new HashMap<>();
        for (int aIdx = 0; aIdx < n; ++aIdx) {
            List<String> acc = accounts.get(aIdx);
            for (int eIdx = 1; eIdx < acc.size(); ++eIdx) {
                String email = acc.get(eIdx);
                // Merge components if email is already in another account
                if (!accountsMap.containsKey(email)) 
                    accountsMap.put(email, aIdx);
                else
                    dsu.unionComponents(aIdx, accountsMap.get(email));
            }
        }

        // Merge emails into their respective component account index
        HashMap<Integer, ArrayList<String>> mergedAccountsMap = new HashMap<>();
        for (Map.Entry<String, Integer> eAndA : accountsMap.entrySet()) {
            String email = eAndA.getKey();
            int paIdx = dsu.findParent(eAndA.getValue());
            mergedAccountsMap.putIfAbsent(paIdx, new ArrayList<String>());
            mergedAccountsMap.get(paIdx).add(email);
        }

        // Reformat merged accounts answer
        List<List<String>> mergedAccounts = new ArrayList<>();
        for (Map.Entry<Integer, ArrayList<String>> aAndEs : mergedAccountsMap.entrySet()) {
            String name = accounts.get(aAndEs.getKey()).get(0);
            List<String> emails = aAndEs.getValue();
            Collections.sort(emails);
            emails.add(0, name);
            mergedAccounts.add(emails);
        }
        return mergedAccounts;
    }
}

class TestCases {
    public static void main(String[] args) {
        // In terminal:
        // Compile:     "javac Solution.java"
        // Test cases:  "java -ea TestCases"
        List<List<String>> accounts, attempt, answer, answer1, answer2, answer3;

        // Example 1: 
        accounts = Arrays.asList(
            Arrays.asList("John","johnsmith@mail.com","john_newyork@mail.com"),
            Arrays.asList("John","johnsmith@mail.com","john00@mail.com"),
            Arrays.asList("Mary","mary@mail.com"),
            Arrays.asList("John","johnnybravo@mail.com")
        );
        attempt = new Solution().accountsMerge(accounts);
        answer = Arrays.asList(
            Arrays.asList("John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"), 
            Arrays.asList("Mary","mary@mail.com"), 
            Arrays.asList("John","johnnybravo@mail.com")
        );
        assert attempt.equals(answer) : "Expected: " + answer + ", but got: " + attempt;
        // Example 2:
        accounts = Arrays.asList(
            Arrays.asList("Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"), 
            Arrays.asList("Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"), 
            Arrays.asList("Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"), 
            Arrays.asList("Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"), 
            Arrays.asList("Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co")
        );
        attempt = new Solution().accountsMerge(accounts);
        answer1 = Arrays.asList(
            Arrays.asList("Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"),
            Arrays.asList("Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"),
            Arrays.asList("Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"),
            Arrays.asList("Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"),
            Arrays.asList("Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co")
        );
        answer2 = Arrays.asList(
            Arrays.asList("Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"),
            Arrays.asList("Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"), 
            Arrays.asList("Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"), 
            Arrays.asList("Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"), 
            Arrays.asList("Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co")
        );
        answer3 = Arrays.asList(
            Arrays.asList("Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"), 
            Arrays.asList("Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"), 
            Arrays.asList("Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"), 
            Arrays.asList("Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"), 
            Arrays.asList("Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co")
        );
        assert attempt.equals(answer1) || attempt.equals(answer2) || attempt.equals(answer3) : "Expected: " + answer1 + " or " + answer2 + " or " + answer3 + ", but got: " + attempt;
        // Test Case 3:
        accounts = Arrays.asList(
            Arrays.asList("David","David0@m.co","David1@m.co"), 
            Arrays.asList("David","David3@m.co","David4@m.co"), 
            Arrays.asList("David","David4@m.co","David5@m.co"), 
            Arrays.asList("David","David2@m.co","David3@m.co"), 
            Arrays.asList("David","David1@m.co","David2@m.co")
        );
        attempt = new Solution().accountsMerge(accounts);
        answer = Arrays.asList(
            Arrays.asList("David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co")
        );
        assert attempt.equals(answer) : "Expected: " + answer + ", but got: " + attempt;
    }
}