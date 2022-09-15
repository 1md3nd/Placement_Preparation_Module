class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        arr1,arr2 = [], []
        arr = []
        if len(changed) == 1 or len(changed) % 2 != 0:
            return []
        for num in changed:
            if num == 0:
                arr.append(0)
            elif num % 2 == 0 and num != 0:
                arr1.append(num)
            else:
                arr2.append(num)
        # print(arr1,arr2)
        h1 = collections.Counter(arr1)
        h2 = collections.Counter(arr2)
        
        for k2 in arr2:
            if k2*2 in h1 and h1[k2*2] > 0:
                h1[k2*2] -=1
            else:
                return []
        for k1 in sorted(h1.keys()):
            if h1[k1] <= 0:
                continue
            else:
                if k1*2 in h1 and h1[k1*2] > 0:
                    while h1[k1] != 0 and h1[k1*2] != 0:
                        h1[k1*2] -=1
                        h1[k1] -=1
                        arr2.append(k1)
                else:
                    return []
        if len(arr) % 2 == 0:
            for _ in range(len(arr)//2):
                arr2.append(0)
        else:
            return []
        return arr2