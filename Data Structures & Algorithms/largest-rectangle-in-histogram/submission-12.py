class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        stack = [] # Monotonic Stack -> 以遞增的方式保存高度位置
        for i in range(n + 1): # 用於清空堆疊中剩餘的高度位置
            # 若 i == n or 當前高度 < 單調堆疊的頂層元素
            while stack and (i == n or heights[i] < heights[stack[-1]]):
                # 當前被彈出 stack 的高度即可計算以其高度所能延伸的寬度 -> 進而得到其面積
                # 由於被彈出 stack 的高度大於當前頂層高度，因此其可延伸的右區間已經確定
                h = heights[stack.pop()]
                # 左區間根據當前 stack 內的值進型判斷，若為空則表示可延伸到最左(寬度等於 i)
                # 若不為空則只可延伸到堆疊頂部元素的起始位置 - 1
                w = i if not stack else i - stack[-1] - 1 
                # 判斷與更新最大面積
                max_area = max(max_area, h * w)
            # 存入高度的 index 
            stack.append(i)
        return max_area 
