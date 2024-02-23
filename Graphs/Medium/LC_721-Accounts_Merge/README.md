# [LeetCode #721 - Accounts Merge](https://leetcode.com/problems/accounts-merge/)

**Difficulty: `Medium`**

---

Given a list of `accounts` where each element `accounts[i]` is a list of strings, where the first element `accounts[i][0]` is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails **in sorted order**. The accounts themselves can be returned in **any order**.

---

**Example 1:**

Input:
```
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
```
Output:
```
[["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
```
Explanation:  
The first and second John's are the same person as they have the common email "johnsmith@mail.com".  
The third John and Mary are different people as none of their email addresses are used by other accounts.  
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.  

**Example 2:**

Input:
```
accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
```
Output:
```
[["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
```

**Constraints:**
- `1 <= accounts.length <= 1000`
- `2 <= accounts[i].length <= 10`
- `1 <= accounts[i][j].length <= 30`
- `accounts[i][0]` consists of English letters.
- `accounts[i][j]` (for `j > 0`) is a valid email.

### Hints:
- Use a Disjoint Set Union (DSU) data structure to keep of accounts the same email. Use the account indexes as the parent nodes of the DSU.
- Use a Hash Map to map emails to their respective account index and or vice versa.

# [Solutions](https://github.com/Reddimus/LeetCode_Notes/tree/main/Graphs/Medium/LC_721-Accounts_Merge)

### Graphs - Disjoint Set Union (DSU) approach

#### Intuition:
This problem involves merging accounts that share the same email. What is not so clear is that we also have to keep track of emails that share the same component account. The 2 data structures that can help us solve this problem are `Disjoint Set Union (DSU)` and `HashMap`(s). We can solve this problem by using a `Disjoint Set Union (DSU)` data structure to keep track of the components of the accounts. By using Disjoint Set Union we can mark keep track of accounts that share the same email. We can then merge the emails into their respective component account index and reformat the merged accounts answer.

#### Steps:
1. **Map emails to their respective account index**  
    - Create a `DisjointSetUnion` object to keep track of the components of the accounts. By using Disjoint Set Union we can mark keep track of accounts that share the same email.
    - Create a `HashMap` to map emails to their respective account index.
    - Iterate through each account and its emails.
        - If the email is already in the `accountsMap`, merge the components of the current account and the account of the email.
        - Otherwise, add the email to the `accountsMap` with the current account index.
2. **Merge emails into their respective component account index**  
    - Create a `HashMap` to map the component account index to a list of emails. This is essentially our answer in a different format.
    - Iterate through the `accountsMap`'s key-value pairs.
        - Find the parent account index of the current email's account index.
        - Add the email to the list of emails of the parent account index.
3. **Reformat merged accounts answer**
    - Create a list of string lists to store the merged accounts.
    - Iterate through the `mergedAccountsMap`'s key-value pairs.
        - Get the name of the account from the original `accounts` list by using the parent account index with the given `accounts` input of the method.
        - Sort the list of emails.
        - Add the name and sorted emails to the merged accounts list.
    - **Return the merged accounts list**.

#### Complexity Analysis
- Time Complexity: `O(N * E * α(N) + E log E)` ≈ `O(N * E + E log E)`  
- Space Complexity: `O(N + E)`  

Where `N` is the number of accounts, and `E` is the number of emails across all accounts.  
`α(N)` is the Inverse-Ackermann function, which grows very slowly and is less than 5 for any reasonable value of `N`.

## Python Code
```python
class DisjointSetUnion:
    # Initialize nodes to single sized node graphs
    def __init__(self, n: int) -> None:
        self.parent = [*range(n)]
        self.size = [1] * n

    # Recursively find and assign parent of current node
    def findParent(self, v: int) -> int:
        if self.parent[v] == v:
            return v
        # Path compression optimization
        return self.findParent(self.parent[v])
    
    # Attempt to union two components
    def unionComponents(self, a: int, b: int) -> bool:
        a, b = self.findParent(a), self.findParent(b)
        if a == b:  # If nodes are already in same component
            return False
        
        if self.size[a] < self.size[b]:
            a, b = b, a # Union by size optimization
        # Merge smaller component (b) into larger component (a)
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # Map emails to their respective account index
        dsu = DisjointSetUnion(len(accounts))
        accounts_map = {}
        for a_idx, acc in enumerate(accounts):
            for email in acc[1:]:
                # Merge components if email is already in another account
                if email in accounts_map:
                    dsu.unionComponents(a_idx, accounts_map[email])
                else:
                    accounts_map[email] = a_idx

        # Merge emails into their respective component account index
        merged_accounts = defaultdict(list)
        for email, a_idx in accounts_map.items():
            pa_idx = dsu.findParent(a_idx)
            merged_accounts[pa_idx].append(email)

        # Reformat merged accounts answer; name = accounts[a_idx][0]]
        return [[accounts[a_idx][0]] + sorted(emails) for a_idx, emails in merged_accounts.items()]
```

## C++ Code
```cpp
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
            int aIdx = dsu.find_parent(keyAndVal.second);
            mergedAccountsMap[aIdx].emplace_back(email);
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
```

## Java Code
```java
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
            int aIdx = dsu.findParent(eAndA.getValue());
            mergedAccountsMap.putIfAbsent(aIdx, new ArrayList<String>());
            mergedAccountsMap.get(aIdx).add(email);
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
```