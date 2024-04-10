class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        window_size, target = divmod(target, sum(nums))
        if target == 0:
            return n * window_size
        res = inf
        prefix = {0:-1}
        running_sum = 0
        for i, j in enumerate(nums*2):
            running_sum += j
            k = running_sum - target
            
            if k in prefix:
                res = min(res, i - prefix[k])
                
            prefix[running_sum] = i
        if res == inf:
            return -1
        return n * window_size + res
                
        
        
        