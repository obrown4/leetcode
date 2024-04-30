#STATS
#   Runtime         Memory
#   O(n) beats 67%  O(n + m) beats 53%
#Merge Strings Alternatively #1768
def mergeAlternately(word1: str, word2: str) -> str:
    size = len(word2)
    if len(word1) > len(word2):
        size = len(word1)
    result = ""

    for i in range(size):
        if i < len(word1):
            result += word1[i]
        if i < len(word2):
            result += word2[i]
    return result
