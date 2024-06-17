class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def check_leading_z(s):
            if s.startswith('0') and len(s) > 1:
                return False
            else:
                return True
        
        def check_sequence(first, second, z):
            while z:
                next_number = str(int(first) + int(second))
                if not z.startswith(next_number):
                    return False
                first, second = second, next_number
                z = z[len(next_number):]
            return True

        for i in range(1, n):
            for j in range(i + 1, n):
                first, second = num[:i], num[i:j]
                if check_leading_z(first) and check_leading_z(second):
                    if check_sequence(first, second, num[j:]):
                        return True
        return False

