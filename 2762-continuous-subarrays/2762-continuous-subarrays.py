from collections import deque

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        min_dq = deque() 
        max_dq = deque()  
        
        left = 0
        for right in range(n):
            while min_dq and nums[min_dq[-1]] >= nums[right]:
                min_dq.pop()
            min_dq.append(right)
            
            while max_dq and nums[max_dq[-1]] <= nums[right]:
                max_dq.pop()
            max_dq.append(right)
            
            while nums[max_dq[0]] - nums[min_dq[0]] > 2:
                if min_dq[0] == left:
                    min_dq.popleft()
                if max_dq[0] == left:
                    max_dq.popleft()
                left += 1
            count += right - left + 1
        
        return count

