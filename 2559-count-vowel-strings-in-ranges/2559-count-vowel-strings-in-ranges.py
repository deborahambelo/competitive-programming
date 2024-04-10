class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0] * len(words)
        str1 = ["a","e","i","o","u"]
        for i in range(len(words)):
            if words[i][0] in str1 and words[i][-1] in str1:
                prefix[i] = 1
            else:
                prefix[i] = 0
                
        prefix_sum = [0] * (len(prefix) +1)
        prefix_sum[0] = 0
        for i in range(1,len(prefix)+1):
            prefix_sum[i] = prefix_sum[i-1] + prefix[i-1]
        
        
        result = []
        for query in queries:
            left, right = query[0] + 1, query[1] + 1
            result.append(prefix_sum[right] - prefix_sum[left - 1])
        return result
            
            
            
            
        