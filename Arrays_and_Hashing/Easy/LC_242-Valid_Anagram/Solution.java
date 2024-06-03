import java.util.*;

class Solution {
    // Char counting/Hash map approach
    // T & M: O(n), where n is size of largest string of s or t
    public boolean isAnagram(String s, String t){
        if (s.length() != t.length())
            return false;
        Map<Character, Integer> sCount = new HashMap<Character, Integer>();
        Map<Character, Integer> tCount = new HashMap<Character, Integer>();
        // counting chars into s & t HashMaps
        for (int idx = 0; idx < s.length(); idx++){
            char sChar = s.charAt(idx);
            char tChar = t.charAt(idx);
            sCount.put(sChar, sCount.getOrDefault(sChar, 0) + 1);
            tCount.put(tChar, tCount.getOrDefault(tChar, 0) + 1);
        }
        return sCount.equals(tCount);
    }

    /*
    // Sorting approach
    // T: O(n log n), M: O(1), where n is size of largest string of s or t
    public boolean isAnagram(String s, String t){
        if (s.length() != t.length())
            return false;
        // Convert strings to arrays to sort characters and compare
        char[] sArr = s.toCharArray(), tArr = t.toCharArray();
        Arrays.sort(sArr); 
        Arrays.sort(tArr);
        return Arrays.equals(sArr, tArr);
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
