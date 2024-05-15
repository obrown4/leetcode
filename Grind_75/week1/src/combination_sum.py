#STATS
#   Runtime         Memory
#   O()            O(n)
# Combination Sum #39

def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    res = []

    def dfs(i: int, curr: list[int], total: int) -> None:
        if total == target:
            res.append(curr.copy())
            return
        if total > target or i >= len(candidates):
            return

        curr.append(candidates[i])
        dfs(i, curr, total + candidates[i])
        curr.pop()
        dfs(i + 1, curr, total)
    dfs(0, [], 0)
    return res
