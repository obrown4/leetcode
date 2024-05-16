#STATS
#   Runtime         Memory
#   O(n)            O(n)
# Valid Palindrome #125

def isPalindrome(s: str) -> bool:
    p = preProcess(s)
    l, r = 0, len(p) - 1

    while l < r:
        if p[l] != p[r]:
            return False
        r -= 1
        l+= 1
    return True

def preProcess(s: str) -> list[int]:
    processed = []
    for char in s:
        if char.isalpha():
            processed.append(char.lower())
        if char.isnumeric():
            processed.append(char)
    return processed
