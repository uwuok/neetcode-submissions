from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 將 position 與 speed 依照 position 進行排序（從遠到近）
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd
            # 如果當前車所需時間 > 上一個（即目前 stack top），代表不能追上，形成新 fleet
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
