import heapq
from collections import defaultdict


def printTopK(nums: list, K: int):
    def Counter(collection: list):
        counter = defaultdict(int)
        for x in collection:
            counter[x] += 1
        return counter

    counter = Counter(nums)
    heap = []
    for key in counter:
        heapq.heappush(heap, (-counter[key], key))
    result = []
    for _ in range(K):
        times, key = heapq.heappop(heap)
        result.append(key)
    print(result)


def printDiamond(n: int):
    def format(s: str):
        charArray = [ch for ch in s]
        for i in range(1, len(charArray), 2):
            charArray[i] = ' '
        return ''.join(charArray)

    i = 1
    forward = True
    while i > 0:
        print(' ' * ((2 * n - 1) - (2 * i - 1) // 2), end='')
        print(format('*' * (2 * i - 1)))
        if i == n:
            forward = False
        i = i + 1 if forward else i - 1


def findWords(board: list, words: list):
    trie = defaultdict(dict)
    for word in words:
        node = trie
        for char in word:
            node = node[char]
        node['#'] = True

    def search(x: int, y: int, node: dict, previous: str, visited: set):
        nonlocal result
        if '#' in node:
            result.add(previous)
        for (di, dj) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            i, j = x + di, y + dj
            if -1 < i < rows and -1 < j < cols and board[i][j] in node and (i, j) not in visited:
                search(i, j, node[board[i][j]], previous + board[i][j], visited or {(i, j)})

    rows, cols = len(board), len(board[0])
    result = set()
    for i, j in (i, j for i in range(rows) for j in range(cols)):
        if board[i][j] in trie:
            search(i, j, trie[board[i][j]], board[i][j], {(i, j)})
    return list(result)
