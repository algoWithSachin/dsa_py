"""
Problem:          #42 Trapping Rain Water
Platform:         LeetCode
Difficulty:       Hard

Approach:
  • Initialize two pointers, `l` at the beginning and `r` at the end of the `height` array.
  • Maintain `left_max` and `right_max` to track the maximum height encountered from the left and right sides respectively.
  • While `l` is less than `r`, compare `height[l]` and `height[r]`.
  • If `height[l]` is smaller, calculate water based on `left_max` (add `left_max - height[l]`) and update `left_max` if `height[l]` is greater, then increment `l`.
  • Otherwise (if `height[r]` is smaller or equal), calculate water based on `right_max` (add `right_max - height[r]`) and update `right_max` if `height[r]` is greater, then decrement `r`.

Time Complexity:  O(n)
Space Complexity: O(1)
"""

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        left_max = 0
        right_max = 0
        water = 0

        while l < r:
            if height[l] < height[r]:

                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    water += left_max - height[l]

                l += 1

            else:

                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    water += right_max - height[r]

                r -= 1
        return water