class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = []
        for i in range(len(position)):
            car.append([position[i], speed[i]])
        car.sort(reverse=True)
        stack = []
        for idx, arr in enumerate(car):
            stack.append((target-arr[0]) / arr[1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)