class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_cord = [] 
        for point in points:
            x_cord.append(point[0])
        
        x_cord.sort()  
        
        max_diff = float("-inf")  
        for i in range(len(x_cord) - 1):
            result = x_cord[i+1] - x_cord[i]
            max_diff = max(max_diff, result)  
        return max_diff
