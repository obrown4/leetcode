class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                code = ""
                while stack and stack[-1] != '[':
                    code = stack.pop() + code
                stack.pop()
                num = ""
                while stack and stack[-1].isnumeric():
                    num = stack.pop() + num
                
                stack.append(int(num) * code)
        return "".join(stack)