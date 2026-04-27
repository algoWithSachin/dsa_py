"""
Problem: Is Subsequence
Platform: LeetCode
Difficulty: Easy

Approach:
- Use two pointers to check whether string `s` is a subsequence of string `t`.
- Traverse string `t` while maintaining a pointer `i` for string `s`.
- Whenever characters match, move pointer `i` forward.
- If all characters of `s` are matched (i == len(s)), then `s` is a subsequence of `t`.
- Otherwise, return False.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        
        for char in t:
            if i < len(s) and char == s[i]:
                i += 1
                
        return i == len(s)