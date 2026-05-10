class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 題目：給定一個 int 類型的 array "heights" 其中 heights[i] 表示每個長條的高度，長條的寬度皆為 1
        # Input: [7, 1, 7, 2, 2, 4] 
        # Output: 8 -> 2(height) * 4(7, 2, 2, 4)
        
        # 我可以很簡單的知道單條的高度，但是如果要把寬度考量進來該如何做？
        # ws = [[] for _ in range(len(heights))]
        n = len(heights)
        ws = [0] * len(heights)
        best = max(heights)
        for i in range(len(heights)):
            left = i - 1
            right = i + 1
            m = 9999
            # area = 0
            while left > -1:
                if m > min(heights[left], heights[i]):
                    m = min(heights[left], heights[i])
                area = m * (abs(i - left) + 1)
                if area > best:
                    best = area
                left -= 1
            m = 9999
            while right < n:
                if m > min(heights[right], heights[i]): # m = 2
                    m = min(heights[right], heights[i])
                area = m * (abs(i - right) + 1)
                if area > best:
                    best = area
                right += 1
        return best
                # 
        # 只需要以當前位置的高度進行延伸就好，因為我們會走訪所有的高度，因此只需要以當前的位置高度判斷即可
        # 如果旁邊高度小於當前高度則無需延伸
        # 如果旁邊高度大於或等於當前高度則可以繼續延伸 area = 當前高度 * 延伸距離
    
        # 有些數值我不能考慮進去

