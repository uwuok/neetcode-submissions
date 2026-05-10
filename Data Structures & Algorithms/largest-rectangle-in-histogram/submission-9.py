class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                idx, height = stack.pop()
                area = height * (i - idx)
                max_area = max(max_area, area)
                start = idx
            stack.append((start, h))

        return max_area 