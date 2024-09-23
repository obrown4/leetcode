from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque()
        
        num_dire = 0
        num_radiant = 0

        for s in senate:
            queue.append(s)
            if s == 'D':
                num_dire += 1
            else:
                num_radiant += 1
        
        skip_dire = 0
        skip_radiant = 0

        while num_dire > 0 and num_radiant > 0:
            senator = queue.popleft()
            if senator == 'R':
                if skip_radiant > 0:
                    num_radiant -= 1
                    skip_radiant -= 1
                else:
                    queue.append(senator)
                    skip_dire += 1
            else:
                if skip_dire > 0:
                    num_dire -= 1
                    skip_dire -= 1
                else:
                    queue.append(senator)
                    skip_radiant += 1
        
        if num_dire > 0:
            return "Dire"
        return "Radiant"
                
