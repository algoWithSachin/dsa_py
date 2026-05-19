"""
Problem:          #438 Find All Anagrams in a String
Platform:         LeetCode
Difficulty:       Medium

Approach:
  • Initialize a frequency map (`count`) for string `p` and an empty frequency map (`window`) for the current sliding window in `s`.
  • Pre-populate the `window` map with character counts from the first `len(p)` characters of `s`.
  • Use a sliding window approach with two pointers (`i` for start, `j` for end) and iterate until `j` reaches the end of `s`.
  • In each iteration, check if `window` and `count` are identical. If they are, append the current starting index `i` to the result list.
  • Decrement the count of `s[i]` in `window` (and remove it if count becomes zero), then increment `i` and `j`. If `j` is still valid, increment the count of `s[j]` in `window`.

Time Complexity:  O(len(s) + len(p))
Space Complexity: O(len(s))
"""

from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        count = Counter(p)
        n2 = len(p)
        if len(s) < n2:
            return []
        window = {}
        for i in range(0, n2):
            window[s[i]] = window.get(s[i], 0) + 1

        i = 0
        j = n2 -1 
        res = []

        while j < len(s):
            if window == count:
                res.append(i)

            window[s[i]] -= 1
            if window[s[i]] == 0:
                window.pop(s[i])
            
            i += 1
            j += 1
            if j < len(s):
                window[s[j]] = window.get(s[j], 0) + 1  
            

        return res