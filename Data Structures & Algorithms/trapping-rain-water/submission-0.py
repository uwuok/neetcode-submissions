class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        trapped = [0] * len(height)
        l, r = 0, 0
        # 1.找到每個位置左邊最大的值；找到每個位置右邊最大的值
        # 2.min(maxLeft[i], maxRight[i]) - height[i] = 當前區域可容納大小
        for i in range(len(height)):
            maxLeft[i], maxRight[len(height) - 1 - i] = l, r
            if height[i] > l:
                l = height[i]
            if height[len(height) - 1 - i] > r:
                r = height[len(height) - 1 - i]
        print(maxLeft)
        print(maxRight)
        res = 0
        for i in range(len(height)):
            num = min(maxLeft[i], maxRight[i]) - height[i]
            if num > 0:
                res += num
        return res
            
            