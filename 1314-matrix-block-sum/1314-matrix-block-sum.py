class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
        ans = [[0] * m for _ in range(n)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prefix_sum[i][j] = mat[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
        
        def get_rectangle_sum(row1, col1, row2, col2):
            return prefix_sum[row2][col2] - prefix_sum[row2][col1] - prefix_sum[row1][col2] + prefix_sum[row1][col1]
        
        for i in range(n):
            for j in range(m):
                row1 = max(0, i - k)
                row2 = min(n, i + k + 1)
                col1 = max(0, j - k)
                col2 = min(m, j + k + 1)
                ans[i][j] = get_rectangle_sum(row1, col1, row2, col2)
        
        return ans
