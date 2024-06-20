from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        stack = [source]
        visited_set = set()
        
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            if node not in visited_set:
                visited_set.add(node)
                for neighbour in graph[node]:
                    if neighbour not in visited_set:
                        stack.append(neighbour)
        return False
