class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        count = 0
        prefix_odd = [0]  
        prefix_even = [0]  

        for i in range(len(nums)):
            if i % 2 == 0:
                prefix_even.append(prefix_even[-1] + nums[i])
                prefix_odd.append(prefix_odd[-1])
            else:
                prefix_odd.append(prefix_odd[-1] + nums[i])
                prefix_even.append(prefix_even[-1])

        # Iterate through each index
        for i in range(len(nums)):
            # Calculate the sum of elements before and after index i
            left_sum = prefix_even[i] + (prefix_odd[-1] - prefix_odd[i + 1])
            right_sum = prefix_odd[i] + (prefix_even[-1] - prefix_even[i + 1])
            
            # Check if removing the element at index i makes the array fair
            if left_sum == right_sum:
                count += 1
                
        return count
