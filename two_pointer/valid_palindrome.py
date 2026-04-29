"""
Problem:          #125 Valid Palindrome
Platform:         LeetCode
Difficulty:       Easy

Approach:
  • Initialize two pointers, `i` at the beginning and `j` at the end of the string.
  • Iterate while `i` is less than or equal to `j`.
  • Advance `i` past any non-alphanumeric characters from the left, converting the current character at `i` to lowercase.
  • Advance `j` past any non-alphanumeric characters from the right, converting the current character at `j` to lowercase.
  • If both characters at `i` and `j` are alphanumeric and they do not match, return `False`.
  • If they match, move both pointers inward (`i += 1`, `j -= 1`).
  • If the loop completes, return `True` (indicating all alphanumeric characters formed a palindrome).

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        n = len(s)
        i = 0
        j = n - 1

        while i <= j:
            
            p = s[i].lower()
            q = s[j].lower()

            if not p.isalnum():
                i += 1
                continue
            if not q.isalnum():
                j -= 1
                continue

            if p == q:
                i += 1
                j -= 1
            else:
                return False
        return True