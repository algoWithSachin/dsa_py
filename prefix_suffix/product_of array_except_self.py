"""
Problem:          #238 Product of Array Except Self
Platform:         LeetCode
Difficulty:       Medium

Approach:
  • Initialize an output array `res` of the same size as `nums`.
  • Perform a first pass: Fill `res` such that `res[i]` contains the product of all elements to the left of index `i`. Start `res[0]` with 1.
  • Perform a second pass: Initialize a `suffix` product variable to 1. Iterate from the right to the left of the array.
  • In the second pass, update `suffix` by multiplying it with `nums[i+1]` (the element to the right of the current index `i`).
  • Multiply the current `res[i]` (which holds the prefix product) by the `suffix` product to get the final product of elements except `nums[i]`.

Time Complexity:  O(n)
Space Complexity: O(1)
"""
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [0]*n
        res[0] = 1

        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1]

        suffix = 1

        for i in range(n-2, -1, -1):
            suffix *= nums[i+1]
            res[i] *= suffix

        return res