class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (temp, index)
        n = len(temperatures)
        res = [0] * n

        for i in range(n):
            t = temperatures[i]
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append((t, i))
        return res