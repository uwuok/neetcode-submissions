class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            res.append(0)
            for j in range(len(temperatures) - i):
                if temperatures[i] < temperatures[j + i]:
                    res[i] = j
                    break
        return res
