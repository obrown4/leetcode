class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                val = ""

                while stack[-1] != "[":
                    val = stack.pop() + val
                num = ""
                stack.pop()
                while stack and stack[-1].isnumeric():
                    num = stack.pop() + num
                stack.append(val * int(num))
        
        return "".join(stack)