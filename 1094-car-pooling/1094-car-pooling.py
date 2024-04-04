from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Step 1: Check if individual trips exceed capacity
        for trip in trips:
            if trip[0] > capacity:
                return False
        
        # Step 2: Update the interval list based on the trips
        interval_list = [0] * 1001  # Assuming the maximum distance is 1000 km
        for passengers, start, end in trips:
            interval_list[start] += passengers  # Mark the start of a trip
            interval_list[end] -= passengers    # Mark the end of a trip
        
        # Step 3: Calculate the prefix sum to identify points of intersection
        prefix_sum = 0
        for i in range(1001):
            prefix_sum += interval_list[i]
            if prefix_sum > capacity:  # Check if capacity is exceeded
                return False
        
        # Step 4: If no intersection point found, capacity is sufficient
        return True

