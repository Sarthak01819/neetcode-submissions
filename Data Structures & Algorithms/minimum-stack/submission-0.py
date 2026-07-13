class MinStack:

    def __init__(self):
        self.minStack = []

    def push(self, value: int) -> None:
        if not self.minStack:
            currMin = value
        else:
            currMin = min(value, self.minStack[-1][1])
        self.minStack.append((value, currMin))

    def pop(self) -> None:
        self.minStack.pop()

    def top(self) -> int:
        return self.minStack[-1][0]

    def getMin(self) -> int:
        return self.minStack[-1][1]
