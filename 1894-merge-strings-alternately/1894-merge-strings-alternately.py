class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        w1 = w2 = 0

        for i in range(max(len(word1), len(word2))):
            if w1 < len(word1):
                res += word1[w1]
                w1 += 1
            if w2 < len(word2):
                res += word2[w2]
                w2 += 1
        return res