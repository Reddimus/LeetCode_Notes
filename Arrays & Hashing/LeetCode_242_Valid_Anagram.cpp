/*
Leetcode #242 - Valid Anagram prompt:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
*/

// C++ Standard Library includes everything for competitive programming
// #include <bits/stdc++.h>

#include <string>
#include <algorithm>
#include <cassert>
#include <unordered_map>

using namespace std;

class Solution{
public:
    // Char counting/Hash map approach
    // T: O(n), M: O(2n) = O(n), where n is size of s & t
    bool isAnagram(string s, string t){
        // Check if both strs are same size
        if (s.length() != t.length())
            return false;
        // iterate through each char of both strings and count their chars
        unordered_map<char, int> s_cnt, t_cnt;
        for (int idx = 0; idx < s.length(); idx++){
            s_cnt[s[idx]]++;
            t_cnt[t[idx]]++;
        }
        return s_cnt == t_cnt;
    }
    /*
    // Sorting approach
    // T: O(n log n), M: O(1), where n is size of s or t
    bool isAnagram(string s, string t){
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s == t;
    }
    */
};

int main(){
    Solution sol;
    // Ex1
    string s1 = "anagram", t1 = "nagaram";
    assert(sol.isAnagram(s1, t1) == true);
    // Ex2
    string s2 = "rat", t2 = "car";
    assert(sol.isAnagram(s2, t2) == false);
    // Ex3
    string s3 = "Hello", t3 = "Hell";
    assert(sol.isAnagram(s3, t3) == false);
    return 0;
}
