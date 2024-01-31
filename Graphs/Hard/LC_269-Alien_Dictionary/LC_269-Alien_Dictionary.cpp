#include <bits/stdc++.h>

using namespace std;

// Adjacency Graphs - Topological Sort approach
// T: O(N * M + V + E) = O(N * M + 26 + 26) = O(N * M)
// M: O(V + E) = O(26 + 26) = O(1)
// Where N is the number of words, and M is the length of the longest word(s)
// V is the number of vertices (1->26 characters), and E is the number of edges (1->26 characters)

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

int main() {
    vector<string> words;
    string attempt;

    // Example 1:
    words = {"wrt", "wrf", "er", "ett", "rftt"};
    attempt = Solution().alienOrder(words);
    assert(attempt == "wertf");
    // Example 2:
    words = {"z", "x"};
    attempt = Solution().alienOrder(words);
    assert(attempt == "zx");
    // Example 3:
    words = {"z", "x", "z"};
    attempt = Solution().alienOrder(words);
    assert(attempt == "");
    // Test Case 4:
    words = {"z", "z"};
    attempt = Solution().alienOrder(words);
    assert(attempt == "z");
    // Test Case 5:
    words = {"zy", "zx"};
    attempt = Solution().alienOrder(words);
    assert(attempt == "yxz" || attempt == "zyx");
    // Test Case 6:
    words = {"abc", "ab"};
    attempt = Solution().alienOrder(words);
    assert(attempt == "");
    // Test Case 7:
    words = {"ab", "adc"};
    attempt = Solution().alienOrder(words);
    assert(attempt == "abcd" || attempt == "abdc");
    // Test Case 8:
    words = {"x","abcey","eg","zqcawvqjd","inrfvhw","tlfvm","yinwqggytl","aqyanxo","o","ova","cncis","pgxen","lgqb","xmtdbhtzq","qptimnkw","mdafbuim","j"};
    attempt = Solution().alienOrder(words);
    assert(attempt == "");
    
    return 0;
}