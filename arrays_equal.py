from collections import Counter
class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        count_A = Counter(A)
        count_B = Counter(B)
        return count_A == count_B
