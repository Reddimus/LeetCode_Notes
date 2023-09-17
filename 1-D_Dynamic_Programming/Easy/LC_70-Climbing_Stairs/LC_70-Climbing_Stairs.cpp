#include <bits/stdc++.h>
// #include <iostream>
// #include <cassert>

using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if (n <= 3)
            return n;
        // Bottom up approach
        int n1 = 2, n2 = 3;
        for (int stairs = 4; stairs <= n; stairs++) {
            // Shift window right
            int temp = n1 + n2;
            n1 = n2;
            n2 = temp;
        }
        return n2;
    }
};

int main() {
    Solution sol;
    int attempt;
    // Ex1
    attempt = sol.climbStairs(2);
    assert(attempt == 2);
    // Ex2
    attempt = sol.climbStairs(3);
    assert(attempt == 3);
    // Test case 3
    attempt = sol.climbStairs(4);
    assert(attempt == 5);
    // Test case 4
    attempt = sol.climbStairs(5);
    assert(attempt == 8);
}