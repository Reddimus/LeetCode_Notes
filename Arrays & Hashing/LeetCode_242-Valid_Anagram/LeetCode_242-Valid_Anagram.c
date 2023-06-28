/*
Leetcode #242 - Valid Anagram prompt:

Given two strings s and t, return true if t is an anagram of s, and false 
otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly 
once.

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

#include <stdio.h>                  // fprint
#include <stdbool.h>                // booleans
#include <stdlib.h>                 // qsort()
#include <string.h>                 // string functions
#include <assert.h>                 // testcases

// Counting/Array approach
// T: O(n), M: O(n), where n is size of s & t
bool isAnagram(char * s, char * t){
    int s_size = strlen(s), t_size = strlen(t);
    if (s_size != t_size)
        return false;
    // Count up & down for each char in strs into an alphabetical array
    int char_cnt[26] = {0};
    for (int idx = 0; idx < s_size; idx++){
        char_cnt[s[idx] - 'a']++;
        char_cnt[t[idx] - 'a']--;
    }
    // Iteratively check if every letter count was canceled out (0)
    for (char letter = 0; letter < 26; letter++){
        if (char_cnt[letter] != 0)
            return false;
    }
    return true;
}

/*
// Sorting approach

// Comparison function for sorting chars in ascending order
int compareChars(const void* a, const void* b){
    return (*(char*)a - *(char*)b);
}

// T: O(n log n), M: O(1), where n is size of largest string
bool isAnagram(char * s, char * t){
    // Sort string of chars
    qsort(s, strlen(s), sizeof(char), compareChars);
    qsort(t, strlen(t), sizeof(char), compareChars);
    // Compare if sorted chars match
    return strcmp(s, t) == 0;
}
*/


int main(){
    // Ex1
    char s1[] = "anagram", t1[] = "nagaram";
    assert(isAnagram(s1, t1) == true);
    // Ex2
    char s2[] = "rat", t2[] = "car";
    assert(isAnagram(s2, t2) == false);
    // Ex3
    char s3[] = "Hello", t3[] = "Hell";
    assert(isAnagram(s3, t3) == false);

    return 0;
}
