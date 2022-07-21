class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        count = Counter(arr)
        res,i,l = 0,0, len(arr)
        while i < l:
            j,k = i, l-1
            while j < k:
                if arr[i]+arr[j]+arr[k] < target:
                    j += count[arr[j]]
                elif arr[i]+arr[j]+arr[k] > target:
                    k -= count[arr[k]]
                else:
                    if arr[i] != arr[j] != arr[k]:
                        res += count[arr[i]]*count[arr[j]]*count[arr[k]]
                    elif arr[i] == arr[j] != arr[k]:
                        res += count[arr[i]]*(count[arr[i]]-1)*count[arr[k]]//2
                    elif arr[i] != arr[j] == arr[k]:
                        res += count[arr[i]]*count[arr[j]]*(count[arr[j]]-1)//2
                    else:
                        res += count[arr[i]]*(count[arr[i]]-1)*(count[arr[i]]-2)//6
                    j += count[arr[j]]
                    k -= count[arr[k]]
            i += count[arr[i]]
        return res%1000000007