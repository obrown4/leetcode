from collections import defaultdict
class Solution(object):

    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        edges = {(a,b) for  a, b in connections}
        adj_list = {i : [] for i in range(n)}

        for a, b in connections:
            adj_list[a].append(b)
            adj_list[b].append(a)
        print(adj_list)

        visited = set()
        visited.add(0)
        self.changes = 0

        def dfs(city):
            for neighbor in adj_list[city]:
                if neighbor in visited:
                    continue
                
                if (neighbor, city) not in edges:
                    print(neighbor, city)
                    self.changes += 1
                visited.add(neighbor)
                dfs(neighbor)

        dfs(0)
        return self.changes

        