class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack and self.stack[-1][1] < val:
            self.stack.append((val, self.stack[-1][1]))

        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return None


if __name__ == "__main__":
    obj = MinStack()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
