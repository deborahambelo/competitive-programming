class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [ord(char) for char in s]
        prefix = [0] * len(arr)
        
        for shift in shifts:
            fr, to, pos = shift  
            if pos == 0:
                prefix[fr] -= 1
                if to + 1 < len(arr):
                    prefix[to + 1] += 1
            elif pos == 1:
                prefix[fr] += 1
                if to + 1 < len(arr):
                    prefix[to + 1] -= 1
        
       
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]
        print(prefix)
        for i in range(len(arr)):
            arr[i] = (arr[i] - 97 + prefix[i]) %26 + 97
            
        result = ''.join(chr(char) for char in arr)
        return result
            