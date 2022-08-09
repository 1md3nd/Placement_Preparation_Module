class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        MOD = 10 ** 9 + 7
        N = len(arr)
        hash_ = collections.Counter(arr)
        for i in range(N):
            # print(hash_)
            count = 0
            for j in range(0,i):
                # temp = arr[i] % arr[j]
                if arr[i] % arr[j] == 0:
                    temp = arr[i] // arr[j]
                    # print(temp)
                    if temp in hash_:
                        # print(arr[j],temp)
                        count += hash_[arr[j]] * hash_[temp]
            # print(arr[i],count)
            hash_[arr[i]] += count
        # print(hash_)
        return sum(hash_.values()) % MOD
                    