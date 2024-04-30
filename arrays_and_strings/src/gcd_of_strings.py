#STATS
#   Runtime         Memory
#   O(n) beats 55%  O(min(m,n)) beats 26%

#Greatest Common Divisor of Strings #1071
def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""

    gcd = ""
    curr = ""
    size = min(len(str1), len(str2))

    for i in range(size):
        curr += str1[i]
        if len(str1) % (i + 1) == 0 and len(str2) % (i + 1) == 0:
            gcd = curr
    return gcd
