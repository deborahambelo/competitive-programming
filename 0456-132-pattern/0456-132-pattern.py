class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        stack = []
        curMin = nums[0]
        
        for i in range(1, len(nums)):
            n = nums[i]
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and n > stack[-1][1]:
                return True
            stack.append((n, curMin))
            curMin = min(curMin, n)
        
        return False
