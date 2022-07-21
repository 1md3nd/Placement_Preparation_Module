class Solution:
    def maxArea(self, height: List[int]) -> int:
        end = len(height)-1
        start = 0
        max_area = 0
        while end > start:
            max_area = max(max_area, (end-start)*min(height[start],height[end]))
            if height[end] < height[start]:
                end -= 1
            else:
                start += 1
        return max_area