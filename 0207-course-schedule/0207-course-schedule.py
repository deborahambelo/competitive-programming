class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        visited set. ... if a node is to be visited twice it means there is a cycle so return false
        hashmap: stores adjacency list for node and its prerequisites 
        '''
        pre_Req = {i: [] for i in range(numCourses)}
        for i, j in prerequisites:
            pre_Req[i].append(j)
        visited = set()
        def dfs(i):
            if i in visited:
                return False 
            if pre_Req[i] == []:
                return True 
            visited.add(i)  
            for j in pre_Req[i]:
                if not dfs(j):
                    return False  
            visited.remove(i)  
            pre_Req[i] = []  
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False 
        return True
