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
            # 由於是逆序且不可超車的，因此只需要比較 time
            # time <= stack[-1] 表示與前車會同時抵達
            # time > stack[-1] 表示會晚於前車抵達
            if not stack or time > stack[-1]: 
                stack.append(time)
        return len(stack)
