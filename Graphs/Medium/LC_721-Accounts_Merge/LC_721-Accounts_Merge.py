from collections import defaultdict

# Graphs - Disjoint Set Union (DSU) approach
# T: O(N * E * α(N) + E log E) ≈ O(N * E + E log E), M: O(N + E)
# Where N = # of accounts, E = # of emails, α(N) = Inverse Ackermann function

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

# Example 1: 
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
attempt = Solution().accountsMerge(accounts)
answer = [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
assert attempt == answer, f"Expected {answer}, but got {attempt}"
# Example 2:
accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
attempt = Solution().accountsMerge(accounts)
answer1 = [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
answer2 = [["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
assert attempt == answer1 or attempt == answer2, f"Expected {answer1} or {answer2}, but got {attempt}"
# Test Case 3:
accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
attempt = Solution().accountsMerge(accounts)
answer = [["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]
assert attempt == answer, f"Expected {answer}, but got {attempt}"