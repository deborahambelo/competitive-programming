from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_indices = {}
  
        for i, char in enumerate(s):
            last_indices[char] = i
        
        partitions = []
        start = 0
        end = 0
        
   
        for i, char in enumerate(s):
            end = max(end, last_indices[char]) 
            
            if i == end:
                partitions.append(end - start + 1) 
                start = i + 1 
        
        return partitions


