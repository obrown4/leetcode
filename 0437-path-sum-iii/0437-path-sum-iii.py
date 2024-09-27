# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        in_path = defaultdict(int)
        self.count = 0

        def dfs(node, curr_path: int):
            if not node:
                return
            
            curr_path += node.val
            if curr_path == targetSum:
                self.count += 1
            
            self.count += in_path[curr_path - targetSum]
            in_path[curr_path] += 1

            dfs(node.left, curr_path)
            dfs(node.right, curr_path)
            
            in_path[curr_path] -= 1
        
        dfs(root, 0)
        return self.count
