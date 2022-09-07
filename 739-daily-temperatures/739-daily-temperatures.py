class Solution:
    def dailyTemperatures(self, tem: List[int]) -> List[int]:
        N = len(tem)
        stack = []
        index = {}
        arr = [0 for _ in range(N)]
        for i in range(N-1,-1,-1):
            index[tem[i]] = i
            # print(stack,tem[i])
            if not stack:
                stack.append(tem[i])
            else:
                if stack[-1] > tem[i]:
                    arr[i] = 1
                if stack[-1] == tem[i]:
                    if arr[i+1] == 0:
                        arr[i] = 0
                    else:
                        arr[i] = arr[i+1] + 1
                    stack.append(tem[i])
                else:
                    while stack and stack[-1] <= tem[i]:
                        stack.pop()
                    if not stack:
                        arr[i] = 0
                    else:
                        element = stack[-1]
                        idx = index[element]
                        arr[i] = idx - i
                stack.append(tem[i])
                # stack.sort()
        return arr
            