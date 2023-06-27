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

import java.util.*;

class Solution {
    // Char counting/Hash map approach
    // T & M: O(n), where n is size of largest string of s or t
    public boolean isAnagram(String s, String t){
        if (s.length() != t.length())
            return false;
        Map<Character, Integer> s_cnt = new HashMap<Character, Integer>();
        Map<Character, Integer> t_cnt = new HashMap<Character, Integer>();
        // counting chars into s & t dict
        for (int idx = 0; idx < s.length(); idx++){
            char s_char = s.charAt(idx);
            char t_char = t.charAt(idx);
            s_cnt.put(s_char, s_cnt.getOrDefault(s_char, 0) + 1);
            t_cnt.put(t_char, t_cnt.getOrDefault(t_char, 0) + 1);
        }
        return s_cnt.equals(t_cnt);
    }

    /*
    // Sorting approach
    // T: O(n log n), M: O(1), where n is size of largest string of s or t
    public boolean isAnagram(String s, String t){
        if (s.length() != t.length())
            return false;
        // Convert strings to arrays to sort characters and compare
        char[] s_arr = s.toCharArray(), t_arr = t.toCharArray();
        Arrays.sort(s_arr); 
        Arrays.sort(t_arr);
        return Arrays.equals(s_arr, t_arr);
    }
    */

    public static void main(String[] args) {
        // In terminal:
        // Compile:     "javac Solution.java"
        // Test cases:  "java -ea Solution"
        Solution s = new Solution();
        boolean attempt;
        // Ex1
        attempt = s.isAnagram("anagram", "nagaram");
        assert attempt == true : "Expected true but got " + attempt;
        // Ex2
        attempt = s.isAnagram("rat", "car");
        assert attempt == false : "Expected false but got " + attempt;
        // Ex3
        attempt = s.isAnagram("Hello", "He");
        assert attempt == false : "Expected false but got " + attempt;
    }
}
