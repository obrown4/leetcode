# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # understand
        # return longest zig path

        # match
        # dfs tree

        # plan
        # set a state of left or right
        # traverse left and 

        self.max_zig = 0

        def dfs(node, is_right, length) -> None:
            if not node:
                return 
            
            self.max_zig = max(self.max_zig, length)

            if is_right:
                dfs(node.right, False, length + 1)
                dfs(node.left, True, 1)
            else:
                dfs(node.right, False, 1)
                dfs(node.left, True, length + 1)
        dfs(root.left, True, 1)
        dfs(root.right, False, 1)
        return self.max_zig
