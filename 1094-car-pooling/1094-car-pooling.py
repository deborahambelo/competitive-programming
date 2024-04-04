from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Step 1: Initialize variables
        interval_list = [0] * 1001  # Assuming the maximum distance is 1000 km
        
        # Step 2: Update the interval list based on the trips
        for passengers, start, end in trips:
            interval_list[start] += passengers  # Mark the start of a trip
            interval_list[end] -= passengers    # Mark the end of a trip
        
        # Step 3: Check if the capacity is exceeded at any point
        current_passengers = 0
        for passengers in interval_list:
            current_passengers += passengers
            if current_passengers > capacity:
                return False
        
        # Step 4: If no point exceeds capacity, return True
        return True

# Example usage:
solution = Solution()
trips = [[2, 1, 5], [3, 5, 7]]
capacity = 3
print(solution.carPooling(trips, capacity))
