class CQueue:

    def __init__(self):
        self.stackPush = []
        self.stackPop = []

    def appendTail(self, value: int) -> None:
        if self.stackPop:
            self.stackPush += self.stackPop[::-1]
            self.stackPop = []
        self.stackPush += [value]

    def deleteHead(self) -> int:
        if self.stackPush:
            self.stackPop += self.stackPush[::-1]
            self.stackPush = []
        return self.stackPop.pop() if self.stackPop else -1

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
