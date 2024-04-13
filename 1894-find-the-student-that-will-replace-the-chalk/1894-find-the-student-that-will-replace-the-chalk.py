class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix_sum = [0] * (len(chalk) + 1)
        for i in range(len(chalk)):
            prefix_sum[i + 1] = prefix_sum[i] + chalk[i] 
        
        k %= prefix_sum[-1]  
        for i, num in enumerate(prefix_sum): 
            if k < num:
                return i - 1  
