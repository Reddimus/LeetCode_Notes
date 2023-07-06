/*
LeetCode #11 - Valid Palindrome prompt:

A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads 
the same forward and backward. Alphanumeric characters include letters 
and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Discussion
Solutions
Submissions
Input: s = "race a car"
Output: false
Explanation: "raceacar' is not a palindrome.

Example 3:
Input: s = "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
• 1 <= s. length <= 2 * 10^5
• S consists only of printable ASCII characters 
*/

class Solution{
    public boolean isPalindrome(String s){
        int lo = 0, hi = s.length() - 1;
        while (lo < hi){
            Character lo_char = s.charAt(lo), hi_char = s.charAt(hi);
            if (!Character.isLetterOrDigit(lo_char)){
                lo++;
                continue;
            }
            if (!Character.isLetterOrDigit(hi_char)){
                hi--;
                continue;
            }
            if (Character.toLowerCase(lo_char) != Character.toLowerCase(hi_char))
                return false;
            lo++;
            hi--;
        }
        return true;
    }
    
    /*
    // Other way to iterate Two Pointers/elements method
    // T: O(n), M: O(1), where n is length of s
    public boolean isPalindrome(String s){
        int l_idx = 0, r_idx = s.length() - 1;
        while (l_idx < r_idx){
            while (l_idx < r_idx && !isAlphaNum(s.charAt(l_idx)))
                l_idx++;
            while (l_idx < r_idx && !isAlphaNum(s.charAt(r_idx))) 
                r_idx--;
            if (Character.toLowerCase(s.charAt(l_idx)) != Character.toLowerCase(s.charAt(r_idx))) 
                return false;
            l_idx++;
            r_idx--;
        }
        return true;
    }
    private boolean isAlphaNum(char c){
        return ('a' <= Character.toLowerCase(c) && c <= 'z') || ('0' <= c && c <= '9');
    }
    */

    public static void main(String[] args) throws Exception {
        // In terminal:
        // Compile:         "javac Solution.java"
        // Run test cases:  "java -ea Solution"
        Solution sol = new Solution();
        // Ex 1
        assert sol.isPalindrome("A man, a plan, a canal: Panama") == true : "Expected true but got false";
        // Ex 2
        assert sol.isPalindrome("race a car") == false : "Expected false but got true";
        // Ex 3
        assert sol.isPalindrome("") == true : "Expected true but got false";
        // My Ex 1
        assert sol.isPalindrome("cabbac") == true : "Expected true but got false";
        // My Ex 2
        assert sol.isPalindrome("cac") == true : "Expected true but got false";
        // My Ex 3
        assert sol.isPalindrome("012210") == true : "Expected true but got false";
        // My Ex 4
        assert sol.isPalindrome("04104214") == false : "Expected false but got true";
        // My Ex 5
        assert sol.isPalindrome(".,") == true : "Expected true but got false";
    }
}