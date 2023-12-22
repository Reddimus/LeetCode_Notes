class Solution:
    # Time and space complexity: O(n)
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs: list[str]) -> str:
        encode = ""
        for string in strs:
            encode += str(len(string)) + '#' + string
        return encode
    """
    @param: string: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, string: str) -> list[str]:
        decode = []
        idx = 2
        while idx < len(string):
            length = int(string[idx-2])
            decode.append(string[idx:idx+length])
            idx += length + 2
        return decode

# Ex 1
assert Solution().encode(strs = ["lint", "code", "love", "you"]) == "4#lint4#code4#love3#you"
assert Solution().decode(string = "4#lint4#code4#love3#you") == ["lint", "code", "love", "you"]

# Ex 2
assert Solution().encode(strs = ["we", "say", ":", "yes"]) == "2#we3#say1#:3#yes"
assert Solution().decode(string = "2#we3#say1#:3#yes") == ["we", "say", ":", "yes"]

# Test case 3
assert Solution().encode(strs = ["By"]) == "2#By"
assert Solution().decode(string = "2#By") == ["By"]

# Test case 4
assert Solution().encode(strs = ["1"]) == "1#1"
assert Solution().decode(string = "1#1") == ["1"]

# Test case 5
assert Solution().encode(strs = ["1", "5", "6", "9"]) == "1#11#51#61#9"
assert Solution().decode(string = "1#11#51#61#9") == ["1", "5", "6", "9"]
