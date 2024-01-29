#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string alienOrder(vector<string>& words) {
    }
};

int main() {
    vector<string> words;
    string attempt;

    // Example 1
    words = {"wrt", "wrf", "er", "ett", "rftt"};
    attempt = Solution().alienOrder(words);
    assert(attempt == "wertf");
    // Example 2
    words = {"z", "x"};
    attempt = Solution().alienOrder(words);
    assert(attempt == "zx");
    // Example 3
    words = {"z", "x", "z"};
    attempt = Solution().alienOrder(words);
    assert(attempt == "");
    
    return 0;
}