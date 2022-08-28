class Solution:
    def trap(self, height: List[int]) -> int:
        end = len(height)-1
        start = 0
        area = 0
        lmax = 0
        rmax = 0
        while end > start:
            if height[start]<=height[end]:
                if height[start]>lmax:
                    lmax = height[start]
                else:
                    area = area + lmax - height[start]
                start=start+1
            else:
                if (height[end]>rmax):
                    rmax = height[end]
                else:
                    area = area + rmax - height[end]
                end = end-1
        return area