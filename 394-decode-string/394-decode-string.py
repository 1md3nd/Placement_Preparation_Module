class Solution:
    def decodeString(self, s: str) -> str:
        N = len(s)
        temp = ""
        curr = ""
        num = 0
        stack1 = []
        stack2 = []
        for char in s:
            if char == "[":
                stack1.append(num)
                stack2.append(curr)
                num = 0
                curr = ""
            elif char == "]":
                num = stack1.pop()
                if len(curr) == 0:
                    curr = stack2.pop()
                for i in range(num):
                    temp += curr
                curr = stack2.pop() + temp
                temp = ""
                num = 0
            else:
                if char.isdigit():
                    num = num*10 + int(char)
                else:
                    curr += char
        return curr