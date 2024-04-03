class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        res = []
        final = []
        product = 1
        left = 0
        n = len(nums)
        for left in range(n):
                product *= nums[left]
                result.append(product)
        product = 1
        for right in range(n -1 , -1, -1):
                product *= nums[right]
                res.append(product)
        res.reverse()
        for i in range(n):
            if i == 0:
                final.append(res[1])
            elif i == n -1:
                final.append(result[i-1])
            else:
                final.append(result[i-1] * res[i+1])
        
        return final

