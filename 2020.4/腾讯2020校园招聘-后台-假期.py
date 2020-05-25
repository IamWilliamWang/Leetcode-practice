import sys

def dp(day: int, bannedChoice: int) -> int:
    if day >= n:
        return 0
    # 一共三种选择：休息、上班、健身
    potencialResult = []
    potencialResult += [1 + dp(day + 1, 0)]  # 啥都不干，第二天没有禁止的行为
    if bannedChoice != 1 and corp[day] == 1:  # 去上班
        potencialResult += [dp(day + 1, 1)]  # 没有休息，第二天不能上班
    if bannedChoice != 2 and gym[day] == 1:  # 去健身
        potencialResult += [dp(day + 1, 2)]  # 没有休息，第二天不能健身
    return min(potencialResult)

n = int(sys.stdin.readline().strip())
corp = list(map(int, sys.stdin.readline().strip().split()))
gym = list(map(int, sys.stdin.readline().strip().split()))
print(dp(0, 0))
