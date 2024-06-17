class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def is_valid_number(s):
            if s.startswith('0') and len(s) > 1:
                return False
            else:
                return True
        
        def check_sequence(first, second, remaining):
            while remaining:
                next_number = str(int(first) + int(second))
                if not remaining.startswith(next_number):
                    return False
                first, second = second, next_number
                remaining = remaining[len(next_number):]
            return True

        for i in range(1, n):
            for j in range(i + 1, n):
                first, second = num[:i], num[i:j]
                if is_valid_number(first) and is_valid_number(second):
                    if check_sequence(first, second, num[j:]):
                        return True
        return False

