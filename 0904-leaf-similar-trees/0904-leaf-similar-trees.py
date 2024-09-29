# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        tree1 = []
        tree2 = []
        
        def isLeaf(node):
            return not node.left and not node.right
        
        def dfs(node, tree):
            if not node:
                return 
            
            if isLeaf(node):
                tree.append(node.val)
            
            dfs(node.left, tree)
            dfs(node.right, tree)
        
        dfs(root1, tree1)
        dfs(root2, tree2)
        return tree1 == tree2

        