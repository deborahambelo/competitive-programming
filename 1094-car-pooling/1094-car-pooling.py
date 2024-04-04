class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        for trip in trips:
            if trip[0] > capacity:
                return False
        journey = [0] * 1001 
        for n, start, end in trips:
            journey[start] += n  
            journey[end] -= n 
        
        prefix_sum = 0
        for i in range(1001):
            prefix_sum += journey[i]
            if prefix_sum > capacity:
                return False
            
        return True

