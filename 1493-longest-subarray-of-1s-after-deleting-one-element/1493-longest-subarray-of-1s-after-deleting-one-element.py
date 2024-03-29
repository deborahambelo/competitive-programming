from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        longest_window = 0
        start = 0
        
        for i in range(len(nums)):
            zero_count += (nums[i] == 0)
            
            # Shrink the window until the zero counts come under the limit.
            while zero_count > 1:
                zero_count -= (nums[start] == 0)
                start += 1
            
            longest_window = max(longest_window, i - start)
        
        return longest_window

# Test cases
solution = Solution()
print(solution.longestSubarray([1, 1, 0, 1]))  # Output: 3
print(solution.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))  # Output: 5
print(solution.longestSubarray([1, 1, 1]))  # Output: 2
