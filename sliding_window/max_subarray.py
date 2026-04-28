"""
Problem:          #53 Maximum Subarray
Platform:         LeetCode
Difficulty:       Medium

Approach:
  • Initialize `best_sum` to negative infinity to correctly handle arrays with all negative numbers, and `current_sum` to 0.
  • Iterate through each `num` in the input `nums` array.
  • Add the current `num` to `current_sum`.
  • Update `best_sum` by taking the maximum of `current_sum` and the current `best_sum`.
  • If `current_sum` becomes less than 0, reset it to 0. This discards any subarray that would result in a negative prefix sum, effectively starting a new potential subarray from the next element.

Time Complexity:  O(n)
Space Complexity: O(1)
"""

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
    

        best = float('-inf')
        current = 0

        for num in nums:
            
            current += num
            best = max(current, best)
            if current < 0:
                current = 0
        return best