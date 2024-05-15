#STATS
#   Runtime         Memory
#   O(n)            O(n)
# Group Anagrams #49

def gAnagrams(strs: list[str]) -> list[list[str]]:
    str_dict = {}
    res = []
    for s in strs:
       sorted_s = tuple(sorted(s))
       if sorted_s in str_dict:
           str_dict[sorted_s].append(s)
       else:
           str_dict[sorted_s] = [s]

    for val in str_dict.values():
        res.append(val)
    return res
