# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([(root, 1)])
        max_level = 0
        res = []
        while queue:
            node, level = queue.popleft()
            if not node:
                continue

            if level > max_level:
                res.append(node.val)
                max_level = level
            
            queue.append((node.right, level + 1))
            queue.append((node.left, level + 1))
        return res