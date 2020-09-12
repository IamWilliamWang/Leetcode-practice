# 虾皮2：魔法师的位置在M，目标在K。魔法师有三种技能，M *= 2，M + +和M - -。问最少用几次技能能到目标点


def getMinMagicalSteps(M: int, K: int):
    count = 0
    while M != K:
        if M > K:
            M -= 1  # -1卡
            count += 1
        elif abs(2 * M - K) < abs(M + 1 - K):
            M *= 2  # *2卡
            count += 1
        else:
            M += 1  # +1卡
            count += 1
    return count
