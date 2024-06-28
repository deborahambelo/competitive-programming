# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([(root, 0)])
        visited = set()
        res = []
        curr_arr = []
        curr_level = 0
        while queue:
            node, level = queue.popleft()
            if level != curr_level:
                res.append(curr_arr)
                curr_arr = []
                curr_level = level
            
            curr_arr.append(node.val)
            
            if node.left and node.left not in visited:
                queue.append((node.left, level + 1))
                visited.add(node.left)
            
            if node.right and node.right not in visited:
                queue.append((node.right, level + 1))
                visited.add(node.right)

        if curr_arr:
            res.append(curr_arr)
        
        return res

            
        
        