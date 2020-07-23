from test_script import speedtest


class MaxQueue:

    def __init__(self):
        self._queue = []
        self._maxValQueue = []

    def max_value(self) -> int:
        return self._maxValQueue[0] if self._maxValQueue else -1

    def push_back(self, value: int) -> None:
        while self._maxValQueue and self._maxValQueue[-1] < value:
            self._maxValQueue.pop()
        self._queue.append(value)
        self._maxValQueue.append(value)

    def pop_front(self) -> int:
        if not self._maxValQueue:
            return -1
        ret = self._queue.pop(0)
        if ret == self._maxValQueue[0]:
            self._maxValQueue.pop(0)
        return ret


def test(funcList, inputList):
    maxQueue = None
    for i, (fun, value) in enumerate(zip(funcList, inputList)):
        if fun == 'MaxQueue':
            maxQueue = MaxQueue()
            yield None
        elif fun == 'push_back':
            yield maxQueue.push_back(value[0])
        elif fun == 'pop_front':
            yield maxQueue.pop_front()
        elif fun == 'max_value':
            yield maxQueue.max_value()
        else:
            raise ValueError


funs = ["MaxQueue", "push_back", "push_back", "max_value", "pop_front", "max_value"]
inputs = [[], [1], [2], [], [], []]
out = [None, None, None, 2, 1, 2]
speedtest([lambda f, arg: list(test(f, arg)), lambda x, y: out], [funs, inputs])
funs = ["MaxQueue", "pop_front", "max_value"]
inputs = [[], [], []]
out = [None, -1, -1]
speedtest([lambda f, arg: list(test(f, arg)), lambda x, y: out], [funs, inputs])
funs = ["MaxQueue", "max_value", "pop_front", "max_value", "push_back", "max_value", "pop_front", "max_value",
        "pop_front", "push_back", "pop_front", "pop_front", "pop_front", "push_back", "pop_front", "max_value",
        "pop_front", "max_value", "push_back", "push_back", "max_value", "push_back", "max_value", "max_value",
        "max_value", "push_back", "pop_front", "max_value", "push_back", "max_value", "max_value", "max_value",
        "pop_front", "push_back", "push_back", "push_back", "push_back", "pop_front", "pop_front", "max_value",
        "pop_front", "pop_front", "max_value", "push_back", "push_back", "pop_front", "push_back", "push_back",
        "push_back", "push_back", "pop_front", "max_value", "push_back", "max_value", "max_value", "pop_front",
        "max_value", "max_value", "max_value", "push_back", "pop_front", "push_back", "pop_front", "max_value",
        "max_value", "max_value", "push_back", "pop_front", "push_back", "push_back", "push_back", "pop_front",
        "max_value", "pop_front", "max_value", "max_value", "max_value", "pop_front", "push_back", "pop_front",
        "push_back", "push_back", "pop_front", "push_back", "pop_front", "push_back", "pop_front", "pop_front",
        "push_back", "pop_front", "pop_front", "pop_front", "push_back", "push_back", "max_value", "push_back",
        "pop_front", "push_back", "push_back", "pop_front"]
inputs = [[], [], [], [], [46], [], [], [], [], [868], [], [], [], [525], [], [], [], [], [123], [646], [], [229], [],
          [], [], [871], [], [], [285], [], [], [], [], [45], [140], [837], [545], [], [], [], [], [], [], [561], [237],
          [], [633], [98], [806], [717], [], [], [186], [], [], [], [], [], [], [268], [], [29], [], [], [], [], [866],
          [], [239], [3], [850], [], [], [], [], [], [], [], [310], [], [674], [770], [], [525], [], [425], [], [],
          [720], [], [], [], [373], [411], [], [831], [], [765], [701], []]
out = [None, -1, -1, -1, None, 46, 46, -1, -1, None, 868, -1, -1, None, 525, -1, -1, -1, None, None, 646, None, 646,
       646, 646, None, 123, 871, None, 871, 871, 871, 646, None, None, None, None, 229, 871, 837, 285, 45, 837, None,
       None, 140, None, None, None, None, 837, 806, None, 806, 806, 545, 806, 806, 806, None, 561, None, 237, 806, 806,
       806, None, 633, None, None, None, 98, 866, 806, 866, 866, 866, 717, None, 186, None, None, 268, None, 29, None,
       866, 239, None, 3, 850, 310, None, None, 770, None, 674, None, None, 770]
speedtest([lambda f, arg: list(test(f, arg)), lambda x, y: out], [funs, inputs])
