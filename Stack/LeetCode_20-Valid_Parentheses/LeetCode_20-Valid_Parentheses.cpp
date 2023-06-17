/*
LeetCode #20 - Valid Parenthesis prompt:

Given a string s containing just the characters '(', ')', '{', '}', 
'[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
*/

#include <string>
#include <unordered_map>
#include <stack>
#include <cassert>

using namespace std;

class Solution{
public:
    bool isValid(string s){
        unordered_map<char, char> end_pair = {{')', '('}, {']', '['}, {'}', '{'}};
        // if last char ends with an open parenth
        if (end_pair.find(s[s.size() - 1]) == end_pair.end())
            return false;
        stack<char> open_stack;
        for (char c : s){
            // if char is an open parenth
            if (end_pair.find(c) == end_pair.end()){
                open_stack.push(c);
                continue;
            }
            // if close parenth mismatches pair in top of stack
            // or start with end parenth
            if ((open_stack.empty()) || (end_pair[c] != open_stack.top()))
                return false;
            // else pair complete; pop relevant pair
            open_stack.pop();
        }
        return open_stack.empty();
    }
};

int main(){
    Solution s;
    // Ex1
    assert(s.isValid("()") == true);
    // Ex2
    assert(s.isValid("()[]{}") == true);
    // Ex3
    assert(s.isValid("(]") == false);
    // Testcase4
    assert(s.isValid("{([])}") == true);
    // Testcase5
    assert(s.isValid("[(])") == false);
}
