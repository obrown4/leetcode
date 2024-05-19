#STATS
#   Runtime         Memory
#   O(n)            O(n)
# Generate Parentheses #22

def genP(n: int) -> list[str]:
    stack = []
    res = []

    def dfs(open: int, close: int) -> None:
        if open == close == n:
            res.append("".join(stack))
            return
        if open < n:
            stack.append("(")
            dfs(open + 1, close)
            stack.pop()
        if close < open:
            stack.append(")")
            dfs(open, close + 1)
            stack.pop()

    dfs(0, 0)
    return res
