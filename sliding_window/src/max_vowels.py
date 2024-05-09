#STATS
#   Runtime         Memory
#   O(n)            O(1)
# Maximum Number of Vowels in a Substring of Given Length #1456

def maxVowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    window_v = get_max(s, k, vowels)
    max_v = window_v

    for i in range(k, len(s)):
        to_del = s[i - k]
        if to_del in vowels:
            window_v -= 1
        if s[i] in vowels:
            window_v += 1
        if window_v > max_v:
            max_v = window_v
    return max_v

def get_max(s: str, k: int, vowels: set[str]) -> int:
    num_v = 0
    for i in range(0, k):
        if s[i] in vowels:
            num_v += 1
    return num_v
