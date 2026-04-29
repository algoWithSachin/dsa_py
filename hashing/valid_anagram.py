"""
Problem:          #242 Valid Anagram
Platform:         LeetCode
Difficulty:       Easy

Approach:
  • Check if the lengths of the two strings `s` and `t` are different; if so, return False immediately.
  • Initialize a hash map (dictionary in Python) to store character frequencies for string `s`.
  • Iterate through string `s`, incrementing the count for each character in the hash map.
  • Iterate through string `t`, decrementing the count for each character in the hash map. If a character from `t` is not found in the map or its count becomes negative, return False.
  • Finally, iterate through the values in the hash map. If any character count is not zero, return False. Otherwise, return True.

Time Complexity:  O(N)
Space Complexity: O(1)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        if len(s) != len(t):
            return False

        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1
        for ch in t:
            if ch not in seen.keys():
                return False
            seen[ch] = seen.get(ch, 0) - 1

        for val in seen.values():
            if val != 0 :
                return False
        return True