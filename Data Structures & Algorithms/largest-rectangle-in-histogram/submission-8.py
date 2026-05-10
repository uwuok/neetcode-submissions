class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            left, right = i, i
            h = heights[i]

            while left - 1 >= 0 and heights[left - 1] >= h:
                left -= 1

            while right + 1 < len(heights) and heights[right + 1] >= h:
                right += 1
            
            max_area = max(max_area, h * (right - left + 1))

        return max_area