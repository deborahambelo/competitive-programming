class Solution:
  def applyOperations(self, nums: List[int]) -> List[int]:
    final = [0] * len(nums)
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            nums[i] *= 2
            nums[i+1] = 0
    i = 0
    for j in nums:
        if j > 0:
            final[i] = j
            i += 1
            
    return final