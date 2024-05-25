import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> anagramGroups = new HashMap<>();
        for (String str : strs) {
            String countedChars = countChars(str);
            ArrayList<String> group = anagramGroups.getOrDefault(countedChars, new ArrayList<String>());
            group.add(str);
            anagramGroups.put(countedChars, group);
        }
        
        List<List<String>> groupedAnagrams = new ArrayList<>();
        for (ArrayList<String> group : anagramGroups.values()) 
            groupedAnagrams.add(group);
        return groupedAnagrams;
    }
    
    private String countChars(String str) {
        char[] alphabet = new char[26];
        for (int idx = 0; idx < str.length(); idx++) 
            alphabet[str.charAt(idx) - 'a']++;
        return new String(alphabet);
    }
}