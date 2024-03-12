class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs or len(strs) == 1:
            return 0
        
        rows = len(strs)
        cols = len(strs[0])
        count = 0
        
        for col in range(cols):
            for row in range(1, rows):
                if strs[row][col] < strs[row - 1][col]:
                    count += 1
                    break  
                    
        return count