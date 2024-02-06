import java.util.*;

// Adjacency Graphs - Topological Sort approach
// T: O(N * M + V + E) = O(N * M + 26 + 26) = O(N * M)
// M: O(V + E) = O(26 + 26) = O(1)
// Where N is the number of words, and M is the length of the longest word(s)
// V is the number of vertices (1->26 characters), and E is the number of edges (1->26 characters)

class Solution {
    private HashMap<Character, HashSet<Character>> graph = new HashMap<>();
    public String alienOrder(String[] words) {
        // Map chars in lexicographical order: key char < value char
        for (String w : words) 
            for (char c : w.toCharArray()) 
                graph.putIfAbsent(c, new HashSet<>());

        // For each word pair
        for (int wIdx = 0; wIdx < words.length - 1; ++wIdx) {
            String w1 = words[wIdx], w2 = words[wIdx + 1];
            int minLen = Math.min(w1.length(), w2.length());
            // Check if words are lexicographically sorted
            if (w1.length() > w2.length() &&
            w1.substring(0, minLen).equals(w2.substring(0, minLen)))
                return "";
            // Map the 1st different character between the pair
            for (int cIdx = 0; cIdx < minLen; ++cIdx) {
                char c1 = w1.charAt(cIdx), c2 = w2.charAt(cIdx);
                if (c1 != c2) {
                    graph.get(c1).add(c2);
                    break;
                }
            }
        }
        
        // For every character path in the adjacency list
        for (char c : graph.keySet()) 
            // Check if path is in lexicographic order and build reverse topological order
            if (dfs(c))
                return "";

        // Correctly write topological order (reverse) answer
        String answer = "";
        for (int idx = topologicalOrder.size() - 1; idx >= 0; --idx)
            answer += topologicalOrder.get(idx);
        return answer;
    }

    // Search character path if cycle detected & topologically build answer
    private ArrayList<Character> topologicalOrder = new ArrayList<>();
    private HashMap<Character, Character> visited = new HashMap<>();
    private boolean dfs(char c) {
        if (visited.containsKey(c)) {
            if (visited.get(c) == 'c')
                return true;
            if (visited.get(c) == 'v')
                return false;
        }

        visited.put(c, 'c');    // Mark for cycle detection

        for (char adjChar : graph.get(c))
            if (dfs(adjChar))
                return true;
        
        visited.put(c, 'v');    // Mark as visited
        topologicalOrder.add(c);
        return false;
    }
}

class TestCases {
    public static void main(String[] args) {
        // In terminal:
        // Compile:     "javac AlienDictionary.java"
        // Test cases:  "java -ea TestCases"

        String[] words;
        String attempt, answer, answer2, answer3;

        // Example 1:
        words = new String[] {"wrt","wrf","er","ett","rftt"};
        attempt = new Solution().alienOrder(words);
        answer = "wertf";
        assert attempt.equals(answer) : "Expected " + answer + ", but got " + attempt;
        // Example 2:
        words = new String[] {"z","x"};
        attempt = new Solution().alienOrder(words);
        answer = "zx";
        assert attempt.equals(answer) : "Expected " + answer + ", but got " + attempt;
        // Example 3:
        words = new String[] {"z","x","z"};
        attempt = new Solution().alienOrder(words);
        answer = "";
        assert attempt.equals(answer) : "Expected " + answer + ", but got " + attempt;
        // Test Case 4:
        words = new String[] {"z","z"};
        attempt = new Solution().alienOrder(words);
        answer = "z";
        assert attempt.equals(answer) : "Expected " + answer + ", but got " + attempt;
        // Test Case 5:
        words = new String[] {"zy","zx"};
        attempt = new Solution().alienOrder(words);
        answer = "yxz";
        answer2 = "zyx";
        assert attempt.equals(answer) || attempt.equals(answer2) : "Expected " + answer + " or " + answer2 + ", but got " + attempt;
        // Test Case 6:
        words = new String[] {"abc","ab"};
        attempt = new Solution().alienOrder(words);
        answer = "";
        assert attempt.equals(answer) : "Expected " + answer + ", but got " + attempt;
        // Test Case 7:
        words = new String[] {"ab", "adc"};
        attempt = new Solution().alienOrder(words);
        answer = "abcd";
        answer2 = "abdc";
        answer3 = "cbda";
        assert attempt.equals(answer) || attempt.equals(answer2) || attempt.equals(answer3) : "Expected " + answer + " or " + answer2 + " or " + answer3 + ", but got " + attempt;
        // Test Case 8:
        words = new String[] {"x","abcey","eg","zqcawvqjd","inrfvhw","tlfvm","yinwqggytl","aqyanxo","o","ova","cncis","pgxen","lgqb","xmtdbhtzq","qptimnkw","mdafbuim","j"};
        attempt = new Solution().alienOrder(words);
        answer = "";
        assert attempt.equals(answer) : "Expected " + answer + ", but got " + attempt;
    }
}