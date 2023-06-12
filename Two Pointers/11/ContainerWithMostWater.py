class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            area = w * h
            if area > maxArea:
                maxArea = area
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxArea