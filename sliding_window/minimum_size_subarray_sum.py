"""
Problem:          #209 Minimum Size Subarray Sum
Platform:         LeetCode
Difficulty:       Medium

Approach:
  • Initialize `minLen` to positive infinity, `tempSum` to 0, and `i` (left pointer) to 0.
  • Iterate with `j` (right pointer) from the beginning of `nums`, expanding the sliding window by adding `nums[j]` to `tempSum`.
  • While `tempSum` is greater than or equal to `target`:
  •   Update `minLen` with the minimum of its current value and the current window length (`j - i + 1`).
  •   Shrink the window from the left by subtracting `nums[i]` from `tempSum` and incrementing `i`.
  • Return `minLen` if it was updated from infinity, otherwise return 0 (indicating no such subarray exists).

Time Complexity:  O(n)
Space Complexity: O(1)
"""

from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minLen = float("inf")


        i = 0
        tempSum = 0

        for j in range(len(nums)):

            tempSum += nums[j]

            while tempSum >= target:

                minLen = min(minLen, j - i + 1)
                tempSum -= nums[i]

                i += 1

        return 0 if minLen == float("inf") else minLen