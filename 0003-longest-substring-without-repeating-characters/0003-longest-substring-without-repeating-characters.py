class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        adict = defaultdict(int)
        max_len = 0
        for right in range(len(s)):
            adict[s[right]] += 1
            while left < len(s) and len(adict) != (right - left + 1):
                adict[s[left]] -= 1
                if adict[s[left]] == 0:
                    del adict[s[left]]
                left += 1
            max_len = max(max_len, right-left+1)
        return max_len
       