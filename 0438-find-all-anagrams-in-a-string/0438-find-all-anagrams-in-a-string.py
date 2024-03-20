from collections import Counter 
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        k = len(p)
        target = collections.Counter(p)
        win_cnt = collections.Counter(s[:k-1])
        
        for i in range(k-1, len(s)):
            current_char = s[i]
            win_cnt[current_char] += 1
            if win_cnt == target:
                result.append(i - len(p) + 1)
                
            win_cnt[s[i - len(p) + 1]] -= 1
            if win_cnt[s[i - len(p) + 1]] == 0:
                del win_cnt[s[i - len(p) + 1]]
                
        return result
            
            
            
            
    
            
        
        