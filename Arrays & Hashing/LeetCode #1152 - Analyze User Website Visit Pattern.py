'''
LeetCode #1152 - Analyze User Website Visit Pattern prompt:

You are given two string arrays username and website and an integer array timestamp. All the given 
arrays are of the same length and the tuple [username[i], website[i], timestamp[i]] indicates that 
the user username[i] visited the website website[i] at time timestamp[i].

A pattern is a list of three websites (not necessarily distinct).

- For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] 
are all patterns.
The score of a pattern is the number of users that visited all the websites in the pattern in the same 
order they appeared in the pattern.

- For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x 
visited "home" then visited "away" and visited "love" after that.
- Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such 
that x visited "leetcode" then visited "love" and visited "leetcode" one more time after that.
- Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x 
visited "luffy" three different times at different timestamps.
Return the pattern with the largest score. If there is more than one pattern with the same largest score, 
return the lexicographically smallest such pattern.

Example 1:
Input: 
username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], 
timestamp = [1,2,3,4,5,6,7,8,9,10], 
website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: The tuples in this example are:
["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],
["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
The pattern ("home", "about", "career") has score 2 (joe and mary).
The pattern ("home", "cart", "maps") has score 1 (james).
The pattern ("home", "cart", "home") has score 1 (james).
The pattern ("home", "maps", "home") has score 1 (james).
The pattern ("cart", "maps", "home") has score 1 (james).
The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).

Example 2:
Input: 
username = ["ua","ua","ua","ub","ub","ub"], 
timestamp = [1,2,3,4,5,6], 
website = ["a","b","a","a","b","c"]
Output: ["a","b","a"]

Constraints:
3 <= username.length <= 50
1 <= username[i].length <= 10
timestamp.length == username.length
1 <= timestamp[i] <= 10^9
website.length == username.length
1 <= website[i].length <= 10
username[i] and website[i] consist of lowercase English letters.
It is guaranteed that there is at least one user who visited at least three websites.
All the tuples [username[i], timestamp[i], website[i]] are unique.
'''

class Solution:
    # Time complexity:  O(k*n^3), where n is the length of the input arrays, & k is size of unique sites
    # Space complexity: O(n^3)
    def mostVisitedPattern(self, username: list[str], timestamp: list[int], website: list[str]) -> list[str]:
        # Merge data & sort by timestamp into arr of triple tuples
        data = sorted(zip(username, timestamp, website), key=lambda x: x[1])
        # Track user patterns; user (key), [websites] (val)
        user_pat = {}
        for user, time, web in data:
            user_pat[user] = user_pat.get(user, []) + [web]
        # Store and score all possible combinations of user patterns
        pattern_scores, max_score = {}, 0
        for sites in user_pat.values():
            pattern_comb = set()    # store in set to remove duplicate combs per user
            # Iterate through all possible combinations
            for idx_0 in range(len(sites) - 2):
                for idx_1 in range(idx_0 + 1, len(sites) - 1):
                    for idx_2 in range(idx_1 + 1, len(sites)):
                        pattern_comb.add((sites[idx_0], sites[idx_1], sites[idx_2]))
            # score pattern by tracking which pattern comes up the most over all users
            for comb in pattern_comb:
                pattern_scores[comb] = 1 + pattern_scores.get(comb, 0)
                max_score = max(max_score, pattern_scores[comb])
        # Find highest score, if multiple highest score return lexicographically smallest comb
        best_pat = None
        for key, val in pattern_scores.items():
            if val == max_score:
                if best_pat == None:
                    best_pat = key
                best_pat = min(best_pat, key)
        return list(best_pat)

# from collections import defaultdict
# from itertools import combinations

# class Solution:
    # true O(n^2) best case scenario
	# Time complexity: O(n^3 * log n), where N is the length of the input arrays.
	# Space complexity: O(n^3), where N is the length of the input arrays.
#     def mostVisitedPattern(self, username: list[str], timestamp: list[int], website: list[str]) -> list[str]:
#         # Sort the data by timestamp
#         data = sorted(zip(username, timestamp, website), key=lambda x: x[1])
        
#         # Store the patterns and scores for each user
#         user_patterns = defaultdict(list)
#         for user, _, site in data:
#             user_patterns[user].append(site)
        
#         # Store the scores for all possible patterns
#         pattern_scores = defaultdict(int)
#         for sites in user_patterns.values():
#             # Use set to avoid duplicate patterns for one user
#             patterns = set(combinations(sites, 3))
#             for pattern in patterns:
#                 pattern_scores[pattern] += 1
        
#         # Find the pattern with highest score and smallest order
#         max_score = max(pattern_scores.values())
#         best_pattern = min([p for p in pattern_scores if pattern_scores[p] == max_score])
        
#         return list(best_pattern)

# Example 1
username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]
expected = ["home", "about", "career"]
ex1 = Solution().mostVisitedPattern(username, timestamp, website)
assert ex1 == expected, f'expected {expected}, but got {ex1}'

# Example 2
username = ["ua","ua","ua","ub","ub","ub"] 
timestamp = [1,2,3,4,5,6] 
website = ["a","b","a","a","b","c"]
expected = ["a","b","a"]
ex2 = Solution().mostVisitedPattern(username, timestamp, website)
assert ex2 == expected, f'expected {expected}, but got {ex2}'

# Testcase 3
username = ["zkiikgv", "zkiikgv", "zkiikgv", "zkiikgv"]
timestamp = [4, 2, 3, 1]
website = ["wnaaxbfhxp", "mryxsjc", "oz", "wlarkzzqht"]
expected = ['mryxsjc', 'oz', 'wnaaxbfhxp']
ex3 = Solution().mostVisitedPattern(username, timestamp, website)
assert ex3 == expected, f'expected {expected}, but got {ex3}'