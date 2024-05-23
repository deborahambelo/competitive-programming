class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        q = deque([(root, 0)])
        current_level = -1
        leftmost = root.val

        while q:
            node, level = q.popleft()
            if level > current_level:
                current_level = level
                leftmost = node.val
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return leftmost
