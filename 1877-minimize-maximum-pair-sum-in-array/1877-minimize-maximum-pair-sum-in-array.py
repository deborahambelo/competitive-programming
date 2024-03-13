class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_pair_sum = float('-inf')
        for i in range(len(nums) // 2):
            pair_sum = nums[i] + nums[-i - 1]
            max_pair_sum = max(max_pair_sum, pair_sum)
        return max_pair_sum

