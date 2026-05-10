class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1): # 從倒數第二個開始看, i: 今日
            j = i + 1 # j: 隔日
            while j < n and temperatures[i] >= temperatures[j]: # 當今日的溫度大於隔日的溫度
                # 如果今天比右邊那天熱，那就要繼續找「更後面的」有沒有更熱的
                if res[j] == 0: # 如果右邊那天 他自己都找不到比他更熱的天，那我也不用找了 → 放棄，跳出來
                    j = n  # 避免觸發 j < n 
                    break
                # 如果右邊那天是 3 天後才遇到熱的，那我就可以一次跳過去 → 節省時間！
                j += res[j] # 跳步：透過隔日的結果進行跳步

            if j < n:
                res[i] = j - i # 如果我有成功找到一個比我熱的天，那就把我跟那天之間相差的天數記下來
        return res

