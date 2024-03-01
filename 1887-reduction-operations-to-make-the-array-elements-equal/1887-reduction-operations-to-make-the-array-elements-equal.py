from typing import List

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)  # Sort the list in descending order
        operations = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:  # If the current element is smaller than the previous one
                operations += i  # Increment the operations count by the current index
        return operations
