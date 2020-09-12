import sys


def getMaxResult(indexes: list):
    maxBegin, maxLen = 0, 0
    rowFirstIdx = 1 if indexes[0] % 2 else 2
    for i, idx in enumerate(indexes):
        if i == 0:
            if maxLen < (idx - rowFirstIdx) // 2:
                maxLen = (idx - rowFirstIdx) // 2
                maxBegin = rowFirstIdx
        else:
            if maxLen < (idx - indexes[i - 1] - rowFirstIdx) // 2:
                maxLen = (idx - indexes[i - 1] - rowFirstIdx) // 2
                maxBegin = indexes[i - 1] + 2
    return maxBegin, maxLen


n = int(input().strip())
cutIdxes = sorted(map(int, input().strip().split()))[:n] + [101, 102]
odds = []
evens = []
for number in cutIdxes:
    if number % 2:
        odds.append(number)
    else:
        evens.append(number)

maxBeginOdd, maxLenOdd = getMaxResult(odds) if odds else (1, 50)
maxBeginEven, maxLenEven = getMaxResult(evens) if evens else (2, 50)
# if maxLenOdd == maxLenEven:
#     sys.stdout.write('%d %d' % (min(maxBeginOdd, maxBeginEven), maxLenOdd))
# elif maxLenOdd < maxLenEven:
#     sys.stdout.write('%d %d' % (maxBeginEven, maxLenEven))
# else:
#     sys.stdout.write('%d %d' % (maxBeginOdd, maxLenOdd))
answerLen, answerBegin = sorted([(maxLenOdd, maxBeginOdd), (maxLenEven, maxBeginEven)], key=lambda t: -t[0] + 1e-3 * t[1])[0]
sys.stdout.write('%d %d' % (answerBegin, answerLen))
