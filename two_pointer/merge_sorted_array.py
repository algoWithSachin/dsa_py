"""
Problem: Merge Sorted Array
Platform: LeetCode
Difficulty: Easy

Approach:
- We use a reverse two-pointer technique to avoid overwriting elements in nums1.
- Start pointers from the end of both arrays:
    i → last valid element in nums1 (m - 1)
    j → last element in nums2 (n - 1)
    k → last position in nums1 (m + n - 1)

- At each step, compare nums1[i] and nums2[j]:
    - Place the larger element at nums1[k]
    - Move the corresponding pointer (i or j)
    - Move k backward

- If nums2 still has elements left after nums1 is exhausted,
  copy remaining nums2 elements directly.

Key Idea:
We fill nums1 from the back to avoid overwriting valid data.

Time Complexity: O(m + n)
Space Complexity: O(1) - Inplace
"""

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1