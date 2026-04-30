"""
Problem:          #448 Find All Numbers Disappeared in an Array
Platform:         LeetCode
Difficulty:       Easy

Approach:
  • Initialize an empty list `res` to store the disappeared numbers.
  • Iterate through the input array `nums`. For each `num`, calculate the corresponding index `idx = abs(num) - 1`.
  • At the calculated `idx`, modify the value `nums[idx]` by negating it (e.g., `nums[idx] = -abs(nums[idx])`). This marks the number `abs(num)` as encountered.
  • After the first pass, iterate through `nums` again from index `0` to `n-1`.
  • If `nums[i]` is positive, it means the number `i+1` was never encountered in the first pass. Add `i+1` to the `res` list.

Time Complexity:  O(n)
Space Complexity: O(n)
"""
from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for num in nums:
            ind = abs(num) - 1
            nums[ind] = -abs(nums[ind])

        for i in range(n):
            if nums[i]>0:
                res.append(i+1)
        return res