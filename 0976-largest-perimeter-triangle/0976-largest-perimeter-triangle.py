class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        result=0
        nums=sorted(nums)
        for i in range(1,len(nums)+1):
            if i==(len(nums)-1):
                break
            if nums[-i]<nums[-i-1]+nums[-i-2]:
                return nums[-i]+nums[-i-1]+nums[-i-2]
        return result
                        