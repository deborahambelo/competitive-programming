class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []

        m, n = len(mat), len(mat[0])
        result = []

        for d in range(m + n - 1):
            if d % 2 == 0:  # Moving upwards
                i = min(d, m - 1)
                j = d - i
                while i >= 0 and j < n:
                    result.append(mat[i][j])
                    i -= 1
                    j += 1
            else:  # Moving downwards
                j = min(d, n - 1)
                i = d - j
                while j >= 0 and i < m:
                    result.append(mat[i][j])
                    i += 1
                    j -= 1

        return result

