class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, curr):
            if not node:
                return 0
            curr = curr * 10 + node.val
            if not node.left and not node.right:
                return curr
            left_sum = dfs(node.left, curr)
            right_sum = dfs(node.right, curr)
            
            return left_sum + right_sum
        
        return dfs(root, 0)
