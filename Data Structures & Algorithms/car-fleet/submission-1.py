class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 因為不能超車，所以要以一開始離終點最近的為主
        # 由於 position 的位置是亂序的，為了方便處理，我們將其以 position 進行排序
        cars = sorted(zip(position, speed), reverse=True)
        # 使用 stack 紀錄每個 fleet，如果
        stack = []
        for p, s in cars:
            time = (target - p) / s # 計算剩餘時間
            # 前面的判斷用於保證第一次的 fleet 
            # 後面的判斷用於判斷當前位置的剩餘時間是否大於前面位置的剩餘時間，如果大於表示無法組成同一個車隊
            if not stack or time > stack[-1]: 
                stack.append(time)
            # stack 的長度即表示有幾批車隊
        return len(stack)