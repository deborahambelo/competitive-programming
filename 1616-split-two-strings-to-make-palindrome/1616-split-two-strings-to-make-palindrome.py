class Solution(object):
    def checkPalindromeFormation(self, a, b):
        n = len(a) 
        i = 0
        while i <= n/2 and a[i] == b[n-1-i]:
            i += 1
        j = 0
        while j <=n/2 and b[j] == a[n-1-j]:
            j += 1
        ju = max(i, j)
        left = ju
        right = n-1-ju
        while right - left >= 1 and a[left] == a[right]:
            left += 1
            right -= 1
        if right - left < 1:
            return True
        left = ju
        right =n-1-ju
        while right - left >= 1 and b[left] == b[right]:
            left += 1
            right -= 1
        if right - left < 1: 
            return True
        return False