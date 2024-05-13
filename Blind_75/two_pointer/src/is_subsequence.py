#STATS
#   Runtime         Memory
#   O(n)            O(1)
# Is Subsequence #392

def isSubsequence(s: str, t: str) -> bool:
    s_ptr = 0
    t_ptr = 0

    while s_ptr < len(s) and t_ptr < len(t):
        if s[s_ptr] == t[t_ptr]:
            s_ptr += 1
        t_ptr += 1
    if s_ptr == len(s):
        return True
    else:
        return False
