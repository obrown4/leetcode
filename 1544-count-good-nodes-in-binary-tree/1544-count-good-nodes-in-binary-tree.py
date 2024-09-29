# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # understand
        # return number of nodes that are the >= in path from root
        
        # match 
        # dfs 
        # counter of nodes

        # plan
        # maxInPath = -inf
        # if curr_node > max_path 
        # += 1 set maxinpath to curr
        
        self.good_nodes = 0
        def dfs(node, maxInPath) -> None:
            if not node:
                return
            
            if node.val >= maxInPath:
                self.good_nodes += 1
                maxInPath = node.val
            
            dfs(node.left, maxInPath)
            dfs(node.right, maxInPath)
        
        dfs(root, float('-inf'))
        return self.good_nodes