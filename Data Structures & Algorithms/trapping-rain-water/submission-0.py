class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        waterCount = 0
        current = 0
        while l < r:
            if maxL <= maxR:
                l += 1
                current = min(maxL, maxR) - height[l]
                if current >= 1:
                    waterCount += current
                if maxL < height[l]:
                    maxL = height[l]
            else:
                current = min(maxL, maxR) - height[r]
                r -= 1
                if current >= 1:
                    waterCount += current
                if maxR < height[r]:
                    maxR = height[r]
        return waterCount