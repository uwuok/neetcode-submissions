class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best_area = 0
        n = len(heights)
        for i in range(n):
            left, right = i, i
            
            while left - 1 >= 0 and heights[left - 1] >= heights[i]:
                left -= 1
            
            while right + 1 < n and heights[right + 1] >= heights[i]:
                right += 1
            
            area = heights[i] * (right - left + 1)
            if best_area < area:
                best_area = area

        return best_area