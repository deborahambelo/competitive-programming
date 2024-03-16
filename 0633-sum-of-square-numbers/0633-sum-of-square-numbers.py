class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(c ** 0.5)
        while i <= j:
            summ = i*i + j*j
            if summ == c:
                return True
            elif summ < c:
                i += 1
            else:
                j -= 1
        return False
