class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 單調遞增
        stack = [] # pair: index, height
        max_area = 0
        n = len(heights)
        for i in range(n):
            start = i
            height = heights[i]
            while stack and height < stack[-1][1]:
                idx, h = stack.pop() 
                max_area = max(max_area, h * (i - idx))
                start = idx
            stack.append((start, height)) 
        
        print(stack)
        # 剩餘在 stack 內的
        # for i, h in stack:
            # max_area = max(max_area, h * ())
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area