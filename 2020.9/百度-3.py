def main():
    stairCount, maxStep = list(map(int, input().strip().split()))
    result = 0

    def dp(i: int, nots):
        nonlocal result
        if i > stairCount:
            return
        if i == stairCount:
            result += 1
            return
        steps = list(range(1, maxStep + 1))
        for notNum in nots:
            if notNum in steps:
                steps.remove(notNum)
        for step in steps:
            dp(i + step, [nots[1]] + [step])

    dp(0, [-1, -1])
    print(result)


main()
                               