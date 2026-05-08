"""
Problem:          #763 Partition Labels
Platform:         LeetCode
Difficulty:       Medium

Approach:
  • First, create a hash map (dictionary) to store the last occurrence index for each character in the input string 's'.
  • Initialize `left` (start of current partition) and `end` (farthest reach of any character in the current partition) to 0.
  • Iterate through the string 's' using a `right` pointer. For each character encountered, update `end` to be the maximum of its current value and the last occurrence index of the current character from the hash map.
  • If the `right` pointer reaches `end`, it signifies that all characters within the current partition have been fully covered. This marks the end of a valid partition.
  • Calculate the length of the current partition (`right - left + 1`), add it to the result list, and then update `left` to `right + 1` to start the next partition.

Time Complexity:  O(n)
Space Complexity: O(n)
"""


from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
       
        last = {ch : i for i, ch in enumerate(s)}
        res = []
        
        left = 0
        end = 0
        for right, char in enumerate(s):
            end = max(end, last[char])

            if right == end:
                res.append(right-left + 1)
                left = right + 1
        
        return res