#STATS
#   Runtime         Memory
#   O(n)            O(n)
# Valid Parentheses #20

def isValid(s: str) -> bool:
    closeToOpen = {')' : '(', ']' : '[', '}' : '{'}
    p = []

    for sym in s:
        if sym not in closeToOpen:
            p.append(sym)
        elif p and p[-1] == closeToOpen[sym]:
            p.pop()
        else:
            return False

    if p:
        return False
    return True
