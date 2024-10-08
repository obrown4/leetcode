class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # understand
        # how is this represented in a matrix
        # return number of isolated nodes
        # that could be node by itself or a node in a group

        # match
        # tree, set
        # dfs

        # plan
        # create a visited set
        # iterate over the matrix
        # if i != j and grid[i][j] == 1:
        # dfs on node
        

        self.rows = len(isConnected)
        provinced_nodes = set()

        # dfs on node
        def dfs(row) -> None:
            provinced_nodes.add(row)

            for col in range(self.rows):
                if isConnected[row][col] == 1 and col not in provinced_nodes:
                    dfs(col)


        num_provinces = 0
        for r in range(self.rows):
            if r not in provinced_nodes:
                dfs(r)
                num_provinces += 1
        return num_provinces