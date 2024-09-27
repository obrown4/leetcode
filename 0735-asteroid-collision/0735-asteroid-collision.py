class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # iterate over asteroids
        # if curr a is < 0 and top of stack is > 0 comp


        stack = []

        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if -a > stack[-1]:
                    stack.pop()
                    continue
                elif -a == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack