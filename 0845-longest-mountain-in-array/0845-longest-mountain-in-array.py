class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0  # Mountain requires at least 3 elements

        longest_mountain = 0

        # Iterate through the array
        for i in range(1, n - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:  # Find peak of the mountain
                left = right = i  # Initialize left and right pointers

                # Extend left pointer to find increasing sequence
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1

                # Extend right pointer to find decreasing sequence
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                # Calculate length of mountain subarray
                mountain_length = right - left + 1

                # Update longest mountain length
                longest_mountain = max(longest_mountain, mountain_length)

        return longest_mountain
