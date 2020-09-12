import sys


def toTime(sumTime: int) -> str:
    hours = sumTime // 3600
    mins = (sumTime - (hours * 3600)) // 60
    seconds = sumTime % 60
    hours = (hours + 8) % 24
    if hours > 12:
        return '%02d:%02d:%02d pm' % (hours - 12, mins, seconds)
    elif hours == 12:
        return '%02d:%02d:%02d pm' % (hours, mins, seconds)
    else:
        return '%02d:%02d:%02d am' % (hours, mins, seconds)


for round in range(int(sys.stdin.readline().strip())):
    N = int(input().strip())
    singleTimes = list(map(int, sys.stdin.readline().strip().split()))[:N]
    doubleTimes = list(map(int, sys.stdin.readline().strip().split()))[:N - 1] if N > 1 else []
    minTimeSum = 0
    i = 0
    while i < N:
        if i == N - 1:
            minTimeSum += singleTimes[i]
            i += 1
        elif singleTimes[i] + singleTimes[i + 1] > doubleTimes[i]:  # 分别买不如一起买
            minTimeSum += doubleTimes[i]
            i += 2
        else:
            minTimeSum += singleTimes[i]
            i += 1
    print(toTime(minTimeSum))
