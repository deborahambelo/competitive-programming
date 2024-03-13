class Solution:
    def smallestNumber(self, number: int) -> int:
        if number == 0:
            return 0
        symbol = 1 if number > 0 else -1
        number = abs(number)
        digits = []
        while number:
            number, remainder = divmod(number, 10)
            digits.append(remainder)
        
        digits.sort()
        count = len(digits)
        result = 0
        if symbol == -1:
            for i in range(count-1, -1, -1):
                result = result * 10 + digits[i]
            result *= -1
        else:
            index = 0
            while index < count and digits[index] == 0:
                index += 1
            digits[0], digits[index] = digits[index], digits[0]
            for i in range(count):
                result = result * 10 + digits[i]
        
        return result
