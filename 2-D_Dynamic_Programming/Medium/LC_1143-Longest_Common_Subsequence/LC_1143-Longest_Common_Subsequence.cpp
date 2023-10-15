#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        
    }
};

int main() {
    Solution sol;
    int attempt;

    // Ex1
    attempt = sol.longestCommonSubsequence("abcde", "ace");
    assert(attempt == 3);
    // Ex2
    attempt = sol.longestCommonSubsequence("abc", "abc");
    assert(attempt == 3);
    // Ex3
    attempt = sol.longestCommonSubsequence("abc", "def");
    assert(attempt == 0);

    return 0;
}