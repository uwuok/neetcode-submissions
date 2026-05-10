class Solution:
    def maxArea(self, heights: List[int]) -> int:
        heighest = 0
        hi, length = 0, 0
        l, r = 0, len(heights) - 1
        while l < r:
            print(r)
            hi = min(heights[l], heights[r])
            length = r - l
            amount = hi * length
            if amount > heighest:
                heighest = amount
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return heighest