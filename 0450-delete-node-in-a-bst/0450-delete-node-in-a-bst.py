# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # plan
        # find node
        # store parent node of key
        # call delete on key node
        # if right sub tree

        if not root:
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
               return root.right
            elif not root.right:
                return root.left
            self.findMin(root)
            root.right = self.deleteNode(root.right, root.val)
        return root
    
    def findMin(self, root):
        curr = root.right
        while curr.left:
            curr = curr.left
        root.val = curr.val 
        