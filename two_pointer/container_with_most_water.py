"""
Problem: Container With Most Water
Platform: LeetCode
Difficulty: Medium

Approach: Two Pointers (Greedy)

Idea:
We use two pointers from both ends of the array.
At each step, we calculate area and try to maximize it.
We always move the pointer pointing to the smaller height
because height is the limiting factor (bottleneck).

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height) - 1

        while left < right:
            temp = min(height[left], height[right]) * (right - left)
            result = max(result, temp)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result