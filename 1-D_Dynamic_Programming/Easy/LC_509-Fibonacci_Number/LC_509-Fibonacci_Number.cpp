// #include <bits/stdc++.h>
#include <iostream>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
public:
    int fib(int n) {
        if (n <= 1)
            return n;
        
        // Start from 2
        int n0 = 0, n1 = 1;
        for (int num = 2; num <= n; num++) {
            int temp = n0 + n1;
            n0 = n1;
            n1 = temp;
        }
        return n1;
    }

    /*
    // using a vector to show the dp of each number
    int fib(int n) {
        if (n <= 1)
            return n;
        
        vector<int> dp(n+1, 0);
        dp[1] = 1;
        for (int num = 2; num <= n; num++) {
            dp[num] = dp[num-1] + dp[num-2];
        }
        // print vector
        for (int i = 0; i < dp.size(); i++) {
            cout << dp[i] << " ";
        }
        cout << endl;

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