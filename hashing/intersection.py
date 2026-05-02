"""
Problem:          #349 Intersection of Two Arrays 
Platform:         LeetCode
Difficulty:       Easy

Approach:
  • Initialize an empty list `res` to store the intersection elements.
  • Create a hash set `seen` from the elements of `nums1` for efficient O(1) average-case lookups.
  • Iterate through each number `num` in `nums2`.
  • If `num` is found in `seen`, append `num` to `res` and remove `num` from `seen` to correctly handle duplicate frequencies.

Time Complexity:  O(len(nums1) + len(nums2))
Space Complexity: O(len(nums1))
"""
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
   
        res = []
        seen = set(nums1)
        for num in nums2:
            if num in seen:
                res.append(num)
                seen.remove(num)

        return res