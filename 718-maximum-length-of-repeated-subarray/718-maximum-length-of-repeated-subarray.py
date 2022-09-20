class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def find(nums1,nums2):
            M = len(nums1)
            N = len(nums2)
            score = 0
            res = 0
            for i in range(M):
                score = 0
                for j in range(N):
                    if i + j >= M:
                        break
                    if nums1[i+j] == nums2[j]:
                        score +=1
                        res = max(score,res)
                    else:
                        score = 0
            return res
        return max(find(nums1,nums2),find(nums2,nums1))