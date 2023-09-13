# LeetCode #125 - Valid Palindrome

## Difficulty: Easy

https://leetcode.com/problems/valid-palindrome/description/

### Problem Statement

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

### Example 1

**Input**: `s = "A man, a plan, a canal: Panama"`  
**Output**: `true`  
**Explanation**: `"amanaplanacanalpanama"` is a palindrome.

### Example 2

**Input**: `s = "race a car"`  
**Output**: `false`  
**Explanation**: `"raceacar"` is not a palindrome.

### Example 3

**Input**: `s = ""`  
**Output**: `true`  
**Explanation**: `s` is an empty string `""` after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.

### Constraints

- 1 <= s.length <= 2 * 10^5
- `s` consists only of printable ASCII characters

# Solution Explanation

https://github.com/Reddimus/LeetCode_Notes/tree/main/Two_Pointers/Easy/LC_125-Valid_Palindrome

## Approach: 2 pointers with If Continue Statements
#### Intuition
We can check if a string is a palindrome by iterating through the string using 2 pointers, one starting at the beginning of the string and the other starting at the end of the string. We can then check if the characters at the 2 pointers are the same. If they are not, then the string is not a palindrome. If they are the same, then we can move the pointers closer to the middle of the string and repeat the process. We can continue this process until the pointers meet in the middle of the string. If the pointers meet in the middle of the string, then the string is a palindrome.

#### Algorithm
1. Initialize 2 pointers, `lo/left/l_idx` and `hi/right/r_idx`, to the beginning and end of the string, respectively.
2. Iterate through the string, starting at the beginning and end, respectively.
3. If the character at left pointer is not alphanumeric, then increment the left pointer to skip over it.
4. If the character at right pointer is not alphanumeric, then decrement the right pointer to skip over it.
5. If the characters at the left and right pointers are not the same, then return `false`.
6. If the characters at the left and right pointers are the same, then increment the left pointer and decrement the right pointer.
7. Repeat steps 3-6 until the left and right pointers meet in the middle of the string.
8. If the left and right pointers meet in the middle of the string, then return `true`.

### Complexity Analysis
- Time Complexity: `O(n)`, where `n` is the length of the string.
- Space Complexity: `O(1)`.


### Python Solution
```python
class Solution:
	def isPalindrome(self, s: str) -> bool:
		lo, hi = 0, len(s) - 1
		while lo < hi:
			if not s[lo].isalnum():
				lo += 1
				continue
			if not s[hi].isalnum():
				hi -= 1
				continue
			if s[lo].lower() != s[hi].lower():
				return False
			lo += 1
			hi -= 1
		return True
```

### C++ Solution
```cpp
class Solution {
public:
	bool isPalindrome(string s) {
		int l_idx = 0, r_idx = s.size() - 1;
		while (l_idx < r_idx) {
			if (!isalnum(s[l_idx])) {
				l_idx++;
				continue;
			}
			if (!isalnum(s[r_idx])) {
				r_idx--;
				continue;
			}
			if (tolower(s[l_idx]) != tolower(s[r_idx])) {
				return false;
			}
			l_idx++;
			r_idx--;
		}
		return true;
	}
};
```

### C Solution
```c
bool isPalindrome(char * s){
	int l_idx = 0, r_idx = strlen(s) - 1;
	while (l_idx < r_idx) {
		if (!isalnum(s[l_idx])) {
			l_idx++;
			continue;
		}
		if (!isalnum(s[r_idx])) {
			r_idx--;
			continue;
		}
		if (tolower(s[l_idx]) != tolower(s[r_idx])) {
			return false;
		}
		l_idx++;
		r_idx--;
	}
	return true;
}
```

### Java Solution
```java
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
}
```

## Approach: 2 Pointers with Nested while Loops & custom alphanum() function

### Python Solution
```python
class Solution:
	def isPalindrome(self, s: str) -> bool:
		l_idx, r_idx = 0, len(s) - 1
		while l_idx < r_idx:
			while l_idx < r_idx and not self.alphanum(s[l_idx]):
				l_idx += 1
			while l_idx < r_idx and not self.alphanum(s[r_idx]):
				r_idx -= 1
			if s[l_idx].lower() != s[r_idx].lower():
				return False
			l_idx += 1
			r_idx -= 1
		return True

	def alphanum(self, char: str) -> bool:
		return (
			"a" <= char.lower() <= "z"
			or '0' <= char <= '9'
			)

```

### C++ Solution
```cpp
class Solution {
public:
	bool isPalindrome(string s) {
		int l_idx = 0, r_idx = s.size() - 1;
		while (l_idx < r_idx) {
			while (l_idx < r_idx && !alphanum(s[l_idx])) {
				++l_idx;
			}
			while (l_idx < r_idx && !alphanum(s[r_idx])) {
				--r_idx;
			}
			if (tolower(s[l_idx]) != tolower(s[r_idx])) {
				return false;
			}
			++l_idx;
			--r_idx;
		}
		return true;
	}

	bool alphanum(char c) {
		return (
			'a' <= tolower(c) && tolower(c) <= 'z'
			|| '0' <= c && c <= '9'
			);
	}
};
```

### C Solution
```c
bool alphanum(char c) {
	return (
		'a' <= tolower(c) && tolower(c) <= 'z'
		|| '0' <= c && c <= '9'
		);
}

bool isPalindrome(char * s){
	int l_idx = 0, r_idx = strlen(s) - 1;
	while (l_idx < r_idx) {
		while (l_idx < r_idx && !alphanum(s[l_idx])) {
			++l_idx;
		}
		while (l_idx < r_idx && !alphanum(s[r_idx])) {
			--r_idx;
		}
		if (tolower(s[l_idx]) != tolower(s[r_idx])) {
			return false;
		}
		++l_idx;
		--r_idx;
	}
	return true;
}
```

### Java Solution
```java
class Solution {
	public boolean isPalindrome(String s){
		int l_idx = 0, r_idx = s.length() - 1;
		while (l_idx < r_idx){
			while (l_idx < r_idx && !isAlphaNum(s.charAt(l_idx)))
				++l_idx;
			while (l_idx < r_idx && !isAlphaNum(s.charAt(r_idx))) 
				--r_idx;
			if (Character.toLowerCase(s.charAt(l_idx++)) != Character.toLowerCase(s.charAt(r_idx--))) 
				return false;
		}
		return true;
	}
	private boolean isAlphaNum(char c){
		return ('a' <= Character.toLowerCase(c) && c <= 'z') || ('0' <= c && c <= '9');
	}
}
```