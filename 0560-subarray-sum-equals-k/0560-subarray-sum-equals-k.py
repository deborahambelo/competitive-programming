from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_cnt = defaultdict(int)
        sum_cnt[0] = 1
        total_cnt = 0
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum - k in sum_cnt:
                total_cnt += sum_cnt[current_sum - k]
            sum_cnt[current_sum] += 1

        return total_cnt
