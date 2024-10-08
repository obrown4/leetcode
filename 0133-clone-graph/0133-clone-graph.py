"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(curr_node: Optional['Node']):
            if not curr_node:
                return None
            if curr_node in visited:
                return visited[curr_node]
            
            copy = Node(curr_node.val)
            visited[curr_node] = copy
            
            for n in curr_node.neighbors:
                copy.neighbors.append(dfs(n)) 
            return copy

        return dfs(node)