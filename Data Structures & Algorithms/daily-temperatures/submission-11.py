class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        for i in range(0, n - 1, 1):
            for j in range(i + 1, n, 1):
                if temperatures[i] < temperatures[j]:
                    res[i] = j - i
                    break
        return res
