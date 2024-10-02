# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # understand
        # return lca of tree

        # match 
        # dfs

        # plan
        # dfs from root 
        # if the current node is p or q return true
        # otherwise return false
        # the node that return true from both left and right is the lca
        self.lca = None
        def dfs(node) -> bool:
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)

            mid = False
            if node == p or node == q:
                mid = True
            
            if mid + left + right >= 2:
                self.lca = node
            
            return left or right or mid
        
        dfs(root)
        return self.lca