class NumMatrix(object):

    def __init__(self, matrix):
        n, m = len(matrix), len(matrix[0])
        row_prefix = [[0] * m for _ in range(n)]
        col_prefix = [[0] * m for _ in range(n)]
        
        
        for i in range(n):
            for j in range(m):
                if j == 0:
                    row_prefix[i][j] = matrix[i][j]
                else:
                    row_prefix[i][j] = row_prefix[i][j - 1] + matrix[i][j]
        
        self.row_prefix = row_prefix
        
        
        for i in range(n):
            for j in range(m):
                if i == 0:
                    col_prefix[i][j] = row_prefix[i][j]
                else:
                    col_prefix[i][j] = col_prefix[i - 1][j] + row_prefix[i][j]
        self.col_prefix = col_prefix

    def sumRegion(self, row1, col1, row2, col2):
        if row1 == 0 and col1 == 0:
            return self.col_prefix[row2][col2]
        elif row1 == 0:
            return self.col_prefix[row2][col2] - self.col_prefix[row2][col1 - 1]
        elif col1 == 0:
            return self.col_prefix[row2][col2] - self.col_prefix[row1 - 1][col2]
        else:
            return self.col_prefix[row2][col2] - self.col_prefix[row1 - 1][col2] - self.col_prefix[row2][col1 - 1] + self.col_prefix[row1 - 1][col1 - 1]


