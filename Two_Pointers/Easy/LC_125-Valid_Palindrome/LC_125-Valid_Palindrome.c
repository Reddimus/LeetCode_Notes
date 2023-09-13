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
