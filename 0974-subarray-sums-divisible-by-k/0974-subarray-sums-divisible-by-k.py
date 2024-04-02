from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        r_count = defaultdict(int)  
        r_count[0] = 1
        for right in range(len(nums)):
            prefix_sum += nums[right]
            r = prefix_sum % k
            count += r_count[r]
            r_count[r] += 1
        return count
