# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def __init__(self):
        
        self.maxLevelSize = float('-inf')
        self.maxLevel = 0
        
        self.currLevel = 0
        self.currLevelSize = float('-inf')

    def updateLevels(self, level: int) -> None:
        if self.maxLevelSize < self.currLevelSize:
            self.maxLevelSize = self.currLevelSize
            self.maxLevel = self.currLevel
        
        self.currLevel = level
        self.currLevelSize = 0

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # understand
        # return level that has the max sum of nodes

        # match
        # bfs

        # plan
        # set queue with root, 1
        # store curr level and size of level

        self.queue = deque([(root, 1)])
       
        while self.queue:
            node, level = self.queue.popleft()

            if not node:
                continue
            
            if self.currLevel != level:
                self.updateLevels(level)
            
            self.currLevelSize += node.val

            self.queue.append((node.left, level + 1))
            self.queue.append((node.right, level + 1))
        
        self.updateLevels(self.currLevel)
        return self.maxLevel
    

            
