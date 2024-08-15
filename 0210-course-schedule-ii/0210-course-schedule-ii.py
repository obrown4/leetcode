class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {course : [] for course in range(numCourses)}
        in_degrees = [0] * numCourses

        for c, p in prerequisites:
            adj_list[p].append(c)
            in_degrees[c] += 1
        
        course_order = []

        queue = deque(i for i in range(numCourses) if in_degrees[i] == 0)

        while queue:
            course = queue.popleft()
            course_order.append(course)

            for prereq in adj_list[course]:
                in_degrees[prereq] -= 1

                if in_degrees[prereq] == 0:
                    queue.append(prereq)
        
        for deg in in_degrees:
            if deg > 0 :
                return []
        return course_order