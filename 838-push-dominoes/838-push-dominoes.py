class Solution:
    def pushDominoes(self, arr: str) -> str:
        # T: O(n), S: O(1)
        n = len(arr)

        ans = [0 if a == '.' else -1 if a == 'L' else 1 for a in arr]
        closest = -1
        for i in range(n):
            if '.' == arr[i] and closest >= 0:
                ans[i] += 1 / (i - closest)
            else:
                closest = i if 'R' == arr[i] else -1

        closest = -1
        for i in range(n - 1, -1, -1):
            if '.' == arr[i] and closest >= 0:
                ans[i] -= 1 / (closest - i)
            else:
                closest = i if 'L' == arr[i] else -1

        return ''.join(('.' if a == 0 else 'L' if a < 0 else 'R' for a in ans))