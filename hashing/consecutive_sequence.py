"""
Problem:          #525 Contiguous Array
Platform:         LeetCode
Difficulty:       Medium

Approach:
  • Initialize a 'balance' variable to 0, a hash map 'track' with {0: -1} to handle initial subarrays, and 'maxlen' to 0.
  • Iterate through the input array 'nums' using index 'i' and value 'num'.
  • Update 'balance': decrement by 1 if 'num' is 0, increment by 1 if 'num' is 1.
  • If the current 'balance' is already a key in 'track', it means a subarray exists between 'track[balance]' and 'i' with an equal number of 0s and 1s; update 'maxlen' with the maximum length found.
  • If 'balance' is not in 'track', store the current 'balance' and its index 'i' in the 'track' hash map.

Time Complexity:  O(n)
Space Complexity: O(n)
"""

from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        balance =  0
        track = {0 : -1}
        maxlen = 0
        for i, num in enumerate(nums):
            balance += -1 if num == 0 else +1
            if balance in track :
                maxlen = max(maxlen, i - track[balance])
            else:
                track[balance] = i
        return maxlen