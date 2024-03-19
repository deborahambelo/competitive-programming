class Solution(object):

    def findIndices(self, nums, indexDifference,
                    valueDifference):
        min_idx = 0
        max_idx = 0
        
        for i in range(indexDifference, len(nums)):
            if nums[i - indexDifference] < nums[min_idx]:
                min_idx = i - indexDifference
            if nums[i - indexDifference] > nums[max_idx]:
                max_idx = i - indexDifference
            if abs(nums[i] - nums[min_idx]) >= valueDifference:
                return [min_idx, i]
            if abs(nums[i] - nums[max_idx]) >= valueDifference:
                return [max_idx, i]
        return [-1, -1]