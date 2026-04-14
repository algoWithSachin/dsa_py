"""
Problem: 3Sum (LeetCode)
Platform: LeetCode
Difficulty: Medium

Approach:
- Sort the array
- Fix one element and solve remaining using two pointers
- Skip duplicates to avoid repeated triplets
- Move pointers based on sum comparison

Time Complexity: O(n^2)
Space Complexity: O(1) extra space (excluding output)
"""

from typing import List


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return res