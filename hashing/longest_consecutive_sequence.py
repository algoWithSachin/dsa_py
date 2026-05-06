"""
Problem:          #128 Longest Consecutive Sequence
Platform:         LeetCode
Difficulty:       Medium

Approach:
  • Store all numbers from the input list `nums` into a hash set (`seen`) to enable O(1) average time complexity lookups.
  • Initialize `maxlen` to 0 to keep track of the longest sequence found.
  • Iterate through each unique number (`num`) in the `seen` hash set.
  • For each `num`, check if `num - 1` exists in `seen`. If it does, `num` is part of an already-started sequence, so skip it to avoid redundant calculations.
  • If `num - 1` is not in `seen`, it means `num` is the potential start of a new consecutive sequence. Start counting its length by repeatedly checking `current + 1` in `seen`, incrementing `current` and `length` until the sequence ends. Update `maxlen` with the maximum length found.

Time Complexity:  O(N)
Space Complexity: O(N)
"""

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)
        maxlen = 0

        for num in seen:
            
            if (num - 1) in seen:
                continue
            
            length = 1
            current = num
            while (current + 1) in seen:

                length += 1
                current += 1
            maxlen = max(length, maxlen)
        
        return maxlen