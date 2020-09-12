class IntegerQueue:
    def __init__(self):
        self._queue = []
        self._maxIntQueue = []

    def max(self) -> int:
        return self._maxIntQueue[0] if self._maxIntQueue else -1

    def push(self, value: int) -> None:
        while self._maxIntQueue and self._maxIntQueue[-1] < value:
            self._maxIntQueue.pop()
        self._queue.append(value)
        self._maxIntQueue.append(value)

    def pop(self) -> int:
        if not self._maxIntQueue:
            return -1
        ret = self._queue.pop(0)
        if ret == self._maxIntQueue[0]:
            self._maxIntQueue.pop(0)
        return ret
