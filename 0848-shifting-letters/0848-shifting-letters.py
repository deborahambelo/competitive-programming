from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        arr = [ord(char) for char in s]
        arr2 = [0] * len(arr)
        n = len(shifts)
        suffix = [0] * n
        shifts.reverse()
        suffix_sum = 0  
        
        for i in range(n):
            suffix_sum += shifts[i]  # Update suffix sum with current shift value
            suffix[n - 1 - i] = suffix_sum  # Assign cumulative sum to suffix array in reverse order
        
        # Shift characters and handle wrapping around 'z'
        for i in range(len(suffix)):
            # Calculate the shifted ASCII value
            shifted_ascii = (arr[i] - ord('a') + suffix[i]) % 26 + ord('a')
            arr2[i] = shifted_ascii
        
        arr2_str = ''.join(chr(num) for num in arr2)
        
        return arr2_str
