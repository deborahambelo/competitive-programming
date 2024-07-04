class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        n = len(isConnected)
        visited_arr = set()
        graph = defaultdict(list)
        
        for u in range(n):
            for v in range(n):
                if isConnected[u][v] == 1:
                    graph[u].append(v)
                    graph[v].append(u)
        def dfs(node):
            if node in visited_arr:
                return
            visited_arr.add(node)
            for neighbour in graph[node]:
                dfs(neighbour)
        for i in range(n):
            if i in visited_arr:
                continue
            count += 1
            dfs(i)
        return count
               
        
            
        
        
        
        