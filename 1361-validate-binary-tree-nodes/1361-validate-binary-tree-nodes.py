from collections import deque
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        visited = set()
        no_parent = [0] * n
        for i in range(n):
            if leftChild[i] != -1:
                no_parent[leftChild[i]] += 1
            if rightChild[i] != -1:
                no_parent[rightChild[i]] += 1
        root = -1
        for i in range(n):
            if no_parent[i] == 0:
                if root == -1:
                    root = i
                else:
                    return False
            elif no_parent[i] > 1:
                return False
        if root == -1:
            return False     
        visited = set()
        q = deque()
        q.append(root)
        visited.add(root)
        while q:
            node = q.popleft()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in visited:
                        return False
                    visited.add(child)
                    q.append(child)

            
        return len(visited) == n
            
    
        