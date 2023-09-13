// #include <bits/stdc++.h>
#include <string>
#include <cassert>

using namespace std;

class Solution{
public:
    // T: O(n), M: O(1), where n is size of s
    bool isPalindrome(string s){
        int left = 0, right = s.size() - 1;
        // Increment and Decrement chars from both sides of str
        while (left < right){
            // skip characters that are not letters or numbers
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
};

int main(){
    Solution s;
    // Ex1
    assert(s.isPalindrome("A man, a plan, a canal: Panama") == true);
    // Ex2
    assert(s.isPalindrome("race a car") == false);
    // Ex3
    assert(s.isPalindrome("") == true);
}
