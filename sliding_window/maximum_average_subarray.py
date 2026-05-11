"""
Problem:          #643 Maximum Average Subarray I
Platform:         LeetCode
Difficulty:       Easy

Approach:
  • Initialize a sliding window of size `k` and calculate its initial sum. Store this sum in a variable `windowAvg` (to track the maximum sum found) and `previous` (to track the current window's sum).
  • Iterate the right boundary `r` of the window from `k` to `len(nums) - 1`.
  • For each iteration, slide the window by subtracting `nums[l]` (the leftmost element) from `previous` and adding `nums[r]` (the new rightmost element).
  • Update `windowAvg` to be the maximum of its current value and the `previous` sum.
  • After iterating through all possible windows, return `windowAvg / k` as the maximum average.

Time Complexity:  O(n)
Space Complexity: O(1)
"""

from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        l = 0
        r = k

        windowAvg = sum(nums[:k])
        previous = windowAvg
        while r < len(nums):

            previous -= nums[l]
            previous += nums[r]

            windowAvg = max(windowAvg, previous)

            l += 1
            r += 1


        return windowAvg/k