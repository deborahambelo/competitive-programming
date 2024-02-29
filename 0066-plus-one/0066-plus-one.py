class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = []
        for i in digits:
            number.append(i)
        num = int(''.join(map(str, number)))
        num += 1
        result = [int(d) for d in str(num)]
        return result
