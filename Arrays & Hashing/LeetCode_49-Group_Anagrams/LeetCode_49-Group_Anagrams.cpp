/*
Leetcode #49 - Group Anagrams prompt:

Given an array of strings strs, group the anagrams together. You can return 
the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.


Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
*/

#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <cassert>

using namespace std;

class Solution{
public:
    // Count chars approach

    // return a vector that represents an alphabet with char cnts
    // T: O(s), M: O(s), where s size of string
    vector<int> cntChars(string str){
        vector<int> char_cnt(26, 0);
        for (char c : str){
            int alpha_idx = tolower(c) - 'a';
            char_cnt[alpha_idx]++;
        }
        return char_cnt;
    }

    // T: O(n * s), M: O(n), where n is size of strs & s is size of indiv str
    vector<vector<string>> groupAnagrams(vector<string>& strs){
        unordered_map<string, vector<string>> anagrams_map;
        for (string str: strs){
            // convert char cnts from curr string to map-able key ele
            vector<int> char_cnt = cntChars(str);
            string char_cnt_str(char_cnt.begin(), char_cnt.end());
            // Map the char_cnt string as the key category to map matching anagrams
            anagrams_map[char_cnt_str].push_back(str);
        }
        // return a 2D array representing groups of anagrams stored from our anagrams_map values 
        vector<vector<string>> anagrams_arr;
        for (const auto& pair : anagrams_map)
            anagrams_arr.push_back(pair.second);
        return anagrams_arr;

    }

    
    /*
    // Sorting approach; map anagram using matching sorted strings
    // T: O(n * s log s), M: O(n), where n is size of strs & s is size of indiv str
    vector<vector<string>> groupAnagrams(vector<string>& strs){
        unordered_map<string, vector<string>> anagrams_map;
        for (string str : strs){
            // Create a sorted string of the current string 
            string sorted_str = str;
            sort(sorted_str.begin(), sorted_str.end());
            // Map the sorted string as the key category to map matching anagrams
            anagrams_map[sorted_str].push_back(str);
        }
        // return a 2D array representing groups of anagrams stored from our anagrams_map values 
        vector<vector<string>> anagrams_arr;
        for (const auto& pair : anagrams_map)
            anagrams_arr.push_back(pair.second);
        return anagrams_arr;
    }
    */
};

int main() {
    Solution sol;
    // Ex1
    vector<string> ex1 = {"eat","tea","tan","ate","nat","bat"};
    vector<vector<string>> attempt1 = sol.groupAnagrams(ex1);
    vector<vector<string>> ans1 = {{"bat"},{"nat","tan"},{"ate","eat","tea"}}, 
                            ans1_ = {{"eat","tea","ate"},{"tan","nat"},{"bat"}}, 
                            ans1__ = {{"bat"},{"tan","nat"},{"eat","tea","ate"}};
    assert((attempt1 == ans1 || attempt1 == ans1_ || attempt1 == ans1__));

    // Ex2
    vector<string> ex2 = {""};
    vector<vector<string>> attempt2 = sol.groupAnagrams(ex2);
    vector<vector<string>> ans2 = {{""}};
    assert(attempt2 == ans2);

    // Ex3
    vector<string> ex3 = {"a"};
    vector<vector<string>> attempt3 = sol.groupAnagrams(ex3);
    vector<vector<string>> ans3 = {{"a"}};
    assert(attempt3 == ans3);

    // Testcase4
    // Additional test case: all inputs are the same
    vector<string> ex6 = {"abc", "abc", "abc"};
    vector<vector<string>> attempt6 = sol.groupAnagrams(ex6);
    vector<vector<string>> ans6 = {{"abc", "abc", "abc"}};
    assert(attempt6 == ans6);

    return 0;
}
