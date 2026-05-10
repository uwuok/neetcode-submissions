class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 0,  1, 2,  4, 7  # position
        # 1,  2, 9, 2, 1  # speed
        # 10, 5, 1, 3, 3  # cost 

        # 0, 2, 4
        # 2, 3, 1
        # 5, 3, 6
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for p, s in cars:
            time = (target - p) / s
            if not stack or time > stack[-1]: 
                stack.append(time)
        return len(stack)
