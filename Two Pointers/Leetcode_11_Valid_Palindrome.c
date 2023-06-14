/*
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
Input: s = ""
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
• 1 <= s. length <= 2 * 10^5
• S consists only of printable ASCII characters
*/

#include <stdbool.h>    // booleans
#include <string.h>     // strlen()
#include <ctype.h>      // isalnum()
#include <assert.h>     // test cases

bool isPalindrome(char * s){
    int left = 0, right = strlen(s) - 1;
    // Increment and Decrement chars from both sides of str
    while (left < right){
        // Skip chars that are not numbers or alphabetical letters
        while (!isalnum(s[left]) && left < right)
            left++;
        while (!isalnum(s[right]) && left < right)
            right--;
        // Compare characters
        if (tolower(s[left]) != tolower(s[right]))
            return false;
        left++;
        right--;
    }
    return true;
}

int main(){
    // Ex1
    assert(isPalindrome("A man, a plan, a canal: Panama") == true);
    // Ex2
    assert(isPalindrome("race a car") == false);
    // Ex3
    assert(isPalindrome("") == true);
}
