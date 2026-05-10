class TimeMap:

    def __init__(self):
        self.df = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.df:
            self.df[key] = []
        self.df[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # values = self.df.get(key) # 會有錯誤，因為返回的值若不存在會是 None
        values = self.df.get(key, []) # 指定返回的類型為列表
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                l = m + 1
                res = values[m][0]
            else:
                r = m - 1
        return res

