class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        loopQueue = [0, 1]
        top = -1
        for i in range(2, n + 1):
            # loopQueue[top + 1] = loopQueue[top] + loopQueue[top % 2 - 1]
            # top += 1
            # if top >= 0:
            #     top -= len(loopQueue)
            loopQueue.append(loopQueue[-1] + loopQueue[-2])
        return loopQueue[top]


print(Solution().fib(45))
