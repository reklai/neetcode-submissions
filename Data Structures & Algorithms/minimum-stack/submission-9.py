class MinStack:
    def __init__(self):
        self.mini = []
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.mini.append(val)
        else:
            if val < self.mini[-1]:
                self.mini.append(val)
            else: 
                self.mini.append(self.mini[-1])
            self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]