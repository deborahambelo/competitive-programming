class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set(nums)
        if len(nums) != len(my_set):
            print("Duplicates are present")
            return True
        else:
            print("No duplicates are present")
            return False    