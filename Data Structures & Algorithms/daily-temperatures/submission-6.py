class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        # stack 存放較大者，如果遇到更大的就把 stack 清除
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, idx = stack.pop()
                res[idx] = i - idx
            stack.append((t, i))
        return res