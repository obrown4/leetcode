# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1_leafs = []
        tree2_leafs = []

        def isLeaf(node) -> bool:
            return not node.left and not node.right
        
        def getLeafs(node, isTree1) -> None:
            if not node:
                return
            if isLeaf(node):
                if isTree1:
                    tree1_leafs.append(node.val)
                else:
                    tree2_leafs.append(node.val)
            else:
                getLeafs(node.left, isTree1)
                getLeafs(node.right, isTree1)
        
        
        getLeafs(root1, True)
        getLeafs(root2, False)

        if len(tree1_leafs) != len(tree2_leafs):
            return False
        
        for l1, l2 in zip(tree1_leafs, tree2_leafs):
            if l1 != l2:
                return False
        return True
            