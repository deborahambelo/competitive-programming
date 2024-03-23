class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowel_sequence = {'a', 'e', 'i', 'o', 'u'}
        r = l = 0
        max_length = 0
        seen_vowels = set()
        
        while r < len(word):
            if r > 0 and word[r] < word[r - 1]:
                l = r
                seen_vowels.clear()
            
            seen_vowels.add(word[r])
            
            if len(seen_vowels) == 5:
                max_length = max(max_length, r - l + 1)
            
            r += 1
        
        return max_length
