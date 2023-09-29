// #include <bits/stdc++.h>
#include <iostream>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
public:
    // Dynamic programming w/ 2 variables
    // T: O(n), M: O(1)
    int fib(int n) {
        if (n <= 1)
            return n;
        
        // Start from F(2)
        int n0 = 0, n1 = 1;
        for (int num = 2; num <= n; num++) {
            int temp = n0 + n1;
            n0 = n1;
            n1 = temp;
        }
        return n1;
    }

    /*
    // Dynamic programming w/ array approach
    // T: O(n), M: O(n)
    int fib(int n) {
        if (n <= 1)
            return n;
        
        // Start from F(2)
        vector<int> dp = {0, 1};
        for (int num = 2; num <= n; num++) {
            dp.push_back(dp[dp.size() - 2] + dp[dp.size() - 1]);
        }
        return dp[n];
    }
    */
};

int main() {
    Solution sol;
    
    // Ex1
    assert(sol.fib(2) == 1);
    // Ex2
    assert(sol.fib(3) == 2);
    // Ex3
    assert(sol.fib(4) == 3);
}