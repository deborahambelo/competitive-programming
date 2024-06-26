# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        '''
        
        '''
        
        def dfs(node):
            if not node:
                return 0
            
            ans = 0
            
            if (node.val %2 == 0) and node.left and node.left.left:
                ans += node.left.left.val
                
            
            if (node.val %2 == 0) and node.left and node.left.right:
                ans += node.left.right.val
            
            if (node.val %2 == 0) and node.right and node.right.left:
                ans += node.right.left.val

            if (node.val %2 == 0) and node.right and node.right.right:
                ans += node.right.right.val

            ans += dfs(node.left)
            ans += dfs(node.right)
            
            return ans
        
        
        return dfs(root)
            