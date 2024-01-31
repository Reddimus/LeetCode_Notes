# [LeetCode #269 - Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)

**Difficulty: `Hard`**

---

There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings `words` from the alien language's dictionary. Now it is claimed that the strings in `words` are `sorted lexicographically` by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in `words` cannot correspond to any order of letters, return `""`.

Otherwise, return *a string of the unique letters in the new alien language sorted in* ***lexicographically increasing order*** *by the new language's rules.* If there are multiple solutions, return **any of them.**

---

**Example 1:**  
Input:
```
words = ["wrt","wrf","er","ett","rftt"]
```
Output:
```
"wertf"
```

**Example 2:**  
Input:
```
words = ["z","x"]
```
Output:
```
"zx"
```

**Example 3:**  
Input:
```
words = ["z","x","z"]
```
Output:
```
""
```
Explanation: The order is invalid, so return `""`.

**Constraints:**
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists of only lowercase English letters.

---

### Hints:
- **Check if all words are in lexicographical order**: If a previous word is larger than the current word, and the prefix matches, then the ordering is invalid.
- **Build graph in lexicographical order**: Where the a character points to a set of other characters that are lexicographically larger than itself.
- **Topologicaly build the answer**: Using a Depth First Search (DFS) approach, we can build the answer in topological order and check if the character path is in lexicographical order.

# [Solutions](https://github.com/Reddimus/LeetCode_Notes/tree/main/Graphs/Hard/LC_269-Alien_Dictionary)

### Adjacency List Graphs - Topological Sort approach

#### Intuition
In the Alien Dictionary problem, we determine the order of characters in an alien language by analyzing the lexicographical order of given words. The solution involves constructing a directed graph where each node represents a character, and edges represent the lexicographical precedence of one character over another. This graph is built by comparing adjacent words and identifying the first differing character pair, which implies a directed edge from the first to the second character. A Depth First Search (DFS) is employed to perform a topological sort and detect cycles concurrently. If a cycle is detected (indicating an inconsistency in ordering), or if a larger word is a prefix of a smaller word, we return an empty string, signifying an invalid ordering. Otherwise, we can topologically build our answer, which then has to be reversed to obtain the correct order.

#### Steps:
1. **Build adjacency list**:
    - Map every character used in the words array to the key(s).
    - Where the key is lexicographically smaller than the list of value(s) connected.
    - For each word pair, check if words are lexicographically ordered and map the first character that is different between the two words.
2. **Topologicaly build the answer**:
    - Using a Depth First Search (DFS) approach, we can recursively traverse the character's mapped path. The DFS algorithm checks if cycle detected and topologically builds the answer:
        1. If we encounter a character that was marked for cycle detection, then we know that the character path was not in lexicographical order and return true.
        2. If we encounter a character that was marked as visited, we return false to avoid redundant checks.
        3. Mark the character for cycle detection.
        4. For each character in the character's adjacency list:
            - Recursively check if the character path detected a cycle.
        5. Unmark the character for cycle detection and mark the character as visited.
        6. Append the character to the answer string (Topological order).
    - For every key character in the adjacency list, check if the character path is in lexicographical order by calling the DFS function.
3. **Return the topologically sorted answer string in reverse order**

#### Complexity Analysis
- **Time Complexity:** `O(N * M + V + E)` = `O(N * M + 26 + 26)` = `O(N * M)`
- **Space Complexity:** `O(V + E)` = `O(26 + 26)` = `O(1)`

Where `N` is the number of words, `M` is the average length of each word, `V` is the number of vertices, and `E` is the number of edges. In this case, `V` and `E` can be considered constant since the number of characters in the alphabet is fixed at 26.

#### Python Code
```python
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
```

#### C++ Code
```cpp
class Solution {
public:
    string alienOrder(vector<string>& words) {
        // Map chars in lexicographical order: key char < value char
        unordered_map<char, unordered_set<char>> graph;
        for (string& word : words) 
            for (char& c : word)
                graph[c];

        // For each word pair
        for (int wIdx = 0; wIdx < words.size() - 1; ++wIdx) {
            string &w1 = words[wIdx], &w2 = words[wIdx + 1];
            int minLen = min(w1.size(), w2.size());
            // Check if words are lexicographically sorted
            if (w1.size() > w2.size() && 
            w1.substr(0, minLen) == w2.substr(0, minLen)) 
                return "";
            // Map the 1st different character between the pair
            for (int cIdx = 0; cIdx < minLen; ++cIdx) {
                if (w1[cIdx] != w2[cIdx]) {
                    graph[w1[cIdx]].insert(w2[cIdx]);
                    break;
                }
            }
        }

        vector<char> answer;
        unordered_map<char, char> visited;
        // Search char path if cycle detected & topologically build ans
        function<bool(char)> dfs = [&](char c) -> bool {
            if (visited[c] == 'c')
                return true;
            if (visited[c] == 'v')
                return false;

            visited[c] = 'c';       // Mark for cycle detection

            for (const char& adjChar : graph[c])
                if (dfs(adjChar))
                    return true;
            
            visited[c] = 'v';       // Mark as visited
            answer.push_back(c);    // Topological sort order
            return false;
        };

        // For every character path in the adjacency list
        for (const auto& pair : graph) 
            // Check if path is in lexicographic order
            if (dfs(pair.first))
                return "";

        return string(answer.rbegin(), answer.rend());
    }
};
```