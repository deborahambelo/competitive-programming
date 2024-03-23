class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        r, l = 0, 0
        max_length = 0
        sub_arr = set()
        
        while r < len(word):
            if r > 0 and word[r] < word[r - 1]:
                l = r
                sub_arr.clear()
                
            sub_arr.add(word[r])
            
            if len(sub_arr) == 5:
                max_length = max(max_length, r - l + 1)
            
            r += 1
        
        return max_length
