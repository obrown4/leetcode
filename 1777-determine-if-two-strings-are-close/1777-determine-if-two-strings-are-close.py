class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # understand
        # return true if the word can be made operation 1 or 2
        # else return false

        # match
        # sort -> sort strings and play with operations
        # map -> not sure how this could be used

        # plan
        # if different len return False
        # 
        if len(word1) != len(word2):
            return False

        word1_set = set(word1)
        word2_set = set(word2)

        if word1_set - word2_set:
            return False


        freq_1 = [0] * 26
        freq_2 = [0] * 26

        
        for i in range(len(word1)):
            freq_1[ord(word1[i]) - 97] += 1
            freq_2[ord(word2[i]) - 97] += 1
        
        freq_1.sort()
        freq_2.sort()

        for i in range(26):
            if freq_1[i] != freq_2[i]:
                return False
        return True            
       
