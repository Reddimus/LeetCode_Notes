#include <bits/stdc++.h>

using namespace std;

// Graphs - Disjoint Set Union (DSU) approach
// T: O(N * E * α(N) + E log E) ≈ O(N * E + E log E), M: O(N + E)
// Where N = # of accounts, E = # of emails, α(N) = Inverse Ackermann function

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
        // Path compression optimization
        return find_parent(parents[v]);
    }

    // Attempt to union two components
    bool union_components(int a, int b) {
        a = find_parent(a), b = find_parent(b);
        if (a == b) // If nodes are already in same component
            return false;

        if (sizes[a] < sizes[b]) 
            swap(a, b); // Union by size optimization
        // Merge smaller component (b) into larger component (a)
        parents[b] = a;
        sizes[a] += sizes[b];
        return true;
    }
};

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        // Map emails to their respective account index
        const int& n = accounts.size();
        DisjointSetUnion dsu(n);
        unordered_map<string, int> accountsMap;
        for (int aIdx = 0; aIdx < n; ++aIdx) {
            const vector<string>& acc = accounts[aIdx];
            for (int eIdx = 1; eIdx < acc.size(); ++eIdx) {
                const string& email = acc[eIdx];
                // Merge components if email is already in another account
                if (accountsMap.find(email) == accountsMap.end()) 
                    accountsMap[email] = aIdx;
                else 
                    dsu.union_components(aIdx, accountsMap[email]);
            }
        }

        // Merge emails into their respective component account index
        unordered_map<int, vector<string>> mergedAccountsMap;
        for (const auto& keyAndVal : accountsMap) {
            const string& email = keyAndVal.first;
            int paIdx = dsu.find_parent(keyAndVal.second);
            mergedAccountsMap[paIdx].emplace_back(email);
        }

        // Reformat merged accounts answer
        vector<vector<string>> mergedAccounts;
        for (const auto& keyAndVals : mergedAccountsMap) {
            const string& name = accounts[keyAndVals.first][0];
            vector<string> emails = keyAndVals.second;
            sort(emails.begin(), emails.end());
            emails.insert(emails.begin(), name);
            mergedAccounts.emplace_back(emails);
        }
        return mergedAccounts;
    }
};

int main(void) {
    vector<vector<string>> accounts, attempt, answer, answer1, answer2, answer3;

    // Example 1: 
    accounts = {{"John","johnsmith@mail.com","john_newyork@mail.com"},
                {"John","johnsmith@mail.com","john00@mail.com"},
                {"Mary","mary@mail.com"},
                {"John","johnnybravo@mail.com"}};
    attempt = Solution().accountsMerge(accounts);
    answer = {{"John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"},
              {"Mary","mary@mail.com"},
              {"John","johnnybravo@mail.com"}};
    assert(attempt == answer);
    // Example 2:
    accounts = {{"Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"}, 
                {"Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"}, 
                {"Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"}, 
                {"Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"}, 
                {"Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"}};
    attempt = Solution().accountsMerge(accounts);
    answer1 = {{"Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"},
               {"Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"},
               {"Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"},
               {"Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"},
               {"Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"}};
    answer2 = {{"Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"},
                {"Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"}, 
                {"Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"}, 
                {"Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"}, 
                {"Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"}};
    answer3 = {{"Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"}, 
                {"Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"}, 
                {"Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"}, 
                {"Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"}, 
                {"Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"}};
    assert(attempt == answer1 || attempt == answer2 || attempt == answer3);
    // Test Case 3:
    accounts = {{"David","David0@m.co","David1@m.co"}, 
                {"David","David3@m.co","David4@m.co"}, 
                {"David","David4@m.co","David5@m.co"}, 
                {"David","David2@m.co","David3@m.co"}, 
                {"David","David1@m.co","David2@m.co"}};
    attempt = Solution().accountsMerge(accounts);
    answer = {{"David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"}};
    assert(attempt == answer);
    return 0;
}