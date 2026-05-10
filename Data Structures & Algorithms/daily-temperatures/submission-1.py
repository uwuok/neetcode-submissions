class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []

        for i in range(n):
            count = 1
            j = i + 1
            while j < n:
                if temperatures[i] < temperatures[j]:
                    break
                j += 1
                count += 1
            count = 0 if j == n else count
            res.append(count)
        return res