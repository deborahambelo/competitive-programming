class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        direction = [(-1,0), (0,-1), (1,0), (0,1)]

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m and (row, col) not in visited and grid[row][col] == '1'

        visited = set()

        def dfs(row, col):
            visited.add((row, col))
            for d in direction:
                next_row = row + d[0]
                next_col = col + d[1]
                if inbound(next_row, next_col):
                    dfs(next_row, next_col)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    count += 1
        
        return count
