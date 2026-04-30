"""
Problem:          #152 Maximum Product Subarray
Platform:         LeetCode
Difficulty:       Medium

Approach:
  • Initialize `max_product` to negative infinity, and `prefix_product` and `suffix_product` to 1.
  • Iterate through the array from left to right using index `i`.
  • In each iteration, update `prefix_product` by multiplying it with `nums[i]` and `suffix_product` by multiplying it with `nums[n-1-i]` (scanning from right to left).
  • Update `max_product` with the maximum value among `max_product`, `prefix_product`, and `suffix_product`.
  • If `prefix_product` or `suffix_product` becomes 0, reset them to 1 to signify the start of a new subarray product sequence.

Time Complexity:  O(n)
Space Complexity: O(1)
"""


from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxp = float('-inf')
        prefix = 1
        suffix = 1
        for i in range(n):
            prefix *= nums[i]
            suffix *= nums[n-i -1]
            maxp = max(maxp, prefix, suffix)
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            
            

        return maxp