class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        n = len(arr)
        while n > 1:
            max_index = arr.index(max(arr[:n]))
            if max_index != n - 1:
                if max_index != 0:
                    arr[:max_index + 1] = reversed(arr[:max_index + 1])
                    flips.append(max_index + 1)
                arr[:n] = reversed(arr[:n])
                flips.append(n)
            n -= 1
        return flips


