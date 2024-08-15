from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {course : [] for course in range(numCourses)}
        in_degrees = [0] * numCourses

        for course, preq in prerequisites:
            adj_list[preq].append(course)
            in_degrees[course] += 1
        
        queue = deque(i for i in range(numCourses) if in_degrees[i] == 0)

        while queue:
            course = queue.popleft()

            for c in adj_list[course]:
                in_degrees[c] -= 1

                if in_degrees[c] == 0:
                    queue.append(c)
        
        
        for deg in in_degrees:
            if deg > 0:
                return False
        return True
            

