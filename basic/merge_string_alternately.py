"""
Problem: Merge Strings Alternately
Platform: LeetCode
Difficulty: Easy

Approach:
We use two pointers to traverse both strings simultaneously.
At each step, we take one character from word1 and one from word2 alternately.

Once one string is exhausted, we append the remaining characters from the other string.

We store characters in a list (for efficiency) and finally use join() to build the result string.

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        i = 0
        j = 0

        # merge alternately while both strings have characters
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            i += 1

            res.append(word2[j])
            j += 1

        # append remaining characters from word2 (if any)
        while j < len(word2):
            res.append(word2[j])
            j += 1

        # append remaining characters from word1 (if any)
        while i < len(word1):
            res.append(word1[i])
            i += 1

        return "".join(res)