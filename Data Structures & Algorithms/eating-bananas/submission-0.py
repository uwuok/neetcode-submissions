class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 回傳每一小時最少要吃幾根香蕉
        # BUT, 每一個小時只能在同一個 piles 享用香蕉
        # h = 總共有的時間數量
        left, right = 1, max(piles)
        best = max(piles)
        while left <= right:
            mid = (left + right) // 2
            tot = 0
            for i in piles:
                tot += math.ceil(i / mid)
            if tot > h:
                left = mid + 1
            elif tot <= h:
                right = mid - 1
                best = min(best, mid)
        return best
