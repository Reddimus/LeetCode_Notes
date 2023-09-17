// #include <bits/stdc++.h>
#include <iostream>
#include <cassert>

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