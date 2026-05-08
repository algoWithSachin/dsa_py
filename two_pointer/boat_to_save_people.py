"""
Problem:          #881 Boats to Save People
Platform:         LeetCode
Difficulty:       Medium

Approach:
  • Sort the `people` array in ascending order of weights.
  • Initialize two pointers, `left` at the beginning (lightest person) and `right` at the end (heaviest person), and a `boats` counter to zero.
  • Iterate while `left` is less than or equal to `right`:
  •   Increment `boats` count (as the heaviest person at `right` always takes a boat).
  •   If the combined weight of `people[left]` and `people[right]` does not exceed `limit`, then `people[left]` can share the boat with `people[right]`, so increment `left`.
  •   Decrement `right` (the heaviest person has now been placed in a boat).

Time Complexity:  O(N log N)
Space Complexity: O(1)
"""
from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) - 1
        res = 0

        while left <= right:
            if left == right:
                res += 1
                break
    
            if people[left] + people[right] <= limit:          
                left += 1
           
            right -= 1
            res += 1
        return res