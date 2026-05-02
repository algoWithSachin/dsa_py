"""
Problem:          #560 Subarray Sum Equals K
Platform:         LeetCode
Difficulty:       Medium

Approach:
  • Initialize a hash map `seen` to store `prefix_sum -> frequency` pairs, seeding it with `{0: 1}` to account for subarrays starting from index 0.
  • Initialize `count = 0` to store the number of valid subarrays and `prefix = 0` for the current running sum.
  • Iterate through each number `num` in the input array `nums`.
  • Update `prefix` by adding `num`. Calculate `target_prefix = prefix - k`.
  • If `target_prefix` exists in `seen`, add `seen[target_prefix]` to `count`. Then, increment the frequency of the current `prefix` in `seen` (or add it if new).

Time Complexity:  O(n)
Space Complexity: O(n)
"""

from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        seen = {0 : 1}
        prefix = 0
        for num in nums:
            prefix += num

            look = prefix - k

            if look in seen :
                count += seen[look]
            
            if prefix in seen :
                seen[prefix] += 1
            else:
                seen[prefix] = 1
            
        return count