class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        left = 0
        count = 0
        remainder_count = {0: 1}
        for right in range(len(nums)):
            prefix_sum += nums[right]
            r = prefix_sum % k
            if r in remainder_count:
                count += remainder_count[r]
            remainder_count[r] = remainder_count.get(r, 0) + 1
        return count
