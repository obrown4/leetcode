#STATS
#   Runtime         Memory
#   O(n)            O(n)
# Valid Anagram #242
from collections import defaultdict
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_dict = defaultdict(int)
    t_dict = defaultdict(int)

    for s_char, t_char in zip(s, t):
        s_dict[s_char] += 1
        t_dict[t_char] += 1
    for key in s_dict:
        if s_dict[key] != t_dict[key]:
            return False
    return True
