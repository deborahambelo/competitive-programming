class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = [] 
        prefix_sum = 0  
        
        for num in nums:
            prefix_sum += num  
            running_sum.append(prefix_sum)  
        
        return running_sum
