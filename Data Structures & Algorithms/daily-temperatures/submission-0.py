class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for index in range(0, len(temperatures)):
            while stack and temperatures[index] > stack[-1][0]:
                stackV, stackI = stack.pop()
                diff = index - stackI
                res[stackI] = diff
            stack.append([temperatures[index], index])
        return res