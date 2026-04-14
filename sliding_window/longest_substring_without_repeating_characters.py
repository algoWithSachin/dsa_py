"""
Problem: Longest Substring Without Repeating Characters
Platform: LeetCode
Difficulty: Medium

Approach:
- Use sliding window with two pointers.
- Expand `fast` pointer and track characters in a set.
- If duplicate found, shrink window from `slow` until valid.
- Track max window length.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        seen = set()
        result = 0

        for fast in range(len(s)):
            while s[fast] in seen:
                seen.remove(s[slow])
                slow += 1

            seen.add(s[fast])
            result = max(result, fast - slow + 1)

        return result