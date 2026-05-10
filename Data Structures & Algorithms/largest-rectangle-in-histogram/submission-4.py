class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        best = 0
        
        for i in range(n):
            height = heights[i]
            left = i
            right = i
            
            # 往左延伸
            while left - 1 >= 0 and heights[left - 1] >= height:
                left -= 1
            
            # 往右延伸
            while right + 1 < n and heights[right + 1] >= height:
                right += 1
            
            # 計算寬度與面積
            width = right - left + 1
            area = height * width
            best = max(best, area)
        
        return best
