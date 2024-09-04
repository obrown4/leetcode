# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        # flag: 1 - left, 2 - right, 3 - leaf, 4 middle

        right, left, leaves = [], [], []

        def isRoot(node) -> bool:
            return not node.left and not node.right
        def isLeft(flag) -> bool:
            return flag == 1
        def isRight(flag) -> bool:
            return flag == 2
        
        def preOrder(node, flag) -> None:
            if not node:
                return 
            
            if isRoot(node):
                leaves.append(node.val)
                return
            
            if isLeft(flag):
                left.append(node.val)
            elif isRight(flag):
                right.append(node.val)
            
            
            bucket_and_search(node, flag)

        def bucket_and_search(node, flag):
            if isLeft(flag):
                if node.left:
                    preOrder(node.left, flag)
                    preOrder(node.right, 3)
                else:
                    preOrder(node.right, flag)
            elif isRight(flag):
                if node.right:
                    preOrder(node.left, 3)
                    preOrder(node.right, flag)
                else:
                    preOrder(node.left, flag)
            else:
                preOrder(node.left, flag)
                preOrder(node.right, flag)
            

        preOrder(root.left, 1)
        preOrder(root.right, 2)

        return [root.val] + left + leaves + right[::-1]


            