# Adjacency Graphs - Topological Sort approach
# T: O(N * M + V + E) = O(N * M + 26 + 26) = O(N * M)
# M: O(V + E) = O(26 + 26) = O(1)
# Where N is the number of words, and M is the length of the longest word(s)
# V is the number of vertices (1->26 characters), and E is the number of edges (1->26 characters)

class Solution:
    def alienOrder(self, words: list[str]) -> str:
        # Map chars in lexicographical order: key char < value char
        graph = {char: set() for word in words for char in word}
        # For each word pair
        for idx in range(len(words) - 1):
            w1, w2 = words[idx], words[idx + 1]
            min_len = min(len(w1), len(w2))
            # Check if words are lexicographically sorted
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            # Map the 1st different character between the pair
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    graph[c1].add(c2)
                    break
        
        answer, visited = [], {}
        # Search char path if cycle detected & topologically build ans
        def dfs(char: str) -> bool:
            if char in visited:
                return visited[char]
            
            visited[char] = True    # Mark for cycle detection

            for adj_char in graph[char]:
                # if cycle detected
                if dfs(adj_char):
                    return True
                
            visited[char] = False   # Mark as visited
            answer.append(char)     # Topological sort order
            return False

        # For every character path in the adjacency list
        for char in graph.keys():
            # Check if path is in lexicographic order
            if dfs(char):
                return ""

        answer.reverse()
        return "".join(answer)
    
# Example 1:
attempt = Solution().alienOrder(words=["wrt","wrf","er","ett","rftt"])
answer = "wertf"
assert attempt == answer, f"Expected `{answer}`, but got `{attempt}`."
# Example 2:
attempt = Solution().alienOrder(words=["z","x"])
answer = "zx"
assert attempt == answer, f"Expected `{answer}`, but got `{attempt}`."
# Example 3:
attempt = Solution().alienOrder(words=["z","x","z"])
answer = ""
assert attempt == answer, f"Expected `{answer}`, but got `{attempt}`."
# Test Case 4:
attempt = Solution().alienOrder(words=["z","z"])
answer = "z"
assert attempt == answer, f"Expected `{answer}`, but got `{attempt}`."
# Test Case 5:
attempt = Solution().alienOrder(words=["zy","zx"])
answer = "yxz"
assert attempt == answer, f"Expected `{answer}`, but got `{attempt}`."