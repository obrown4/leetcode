# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # understand 
        # find and return the length of the longest path in tree
        # longest path from left + longest path from right 
        # number of edges

        # match
        # dfs
        # go all the way down to the left and then work back to the right

        # plan
        # start at root and continue to dfs while maintaining the length of the longest path
        maxDiameter = [0]

        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            maxDiameter[0] = max(maxDiameter[0], left + right)
            return 1 + max(left, right)
            
            
        dfs(root)
        return maxDiameter[0]