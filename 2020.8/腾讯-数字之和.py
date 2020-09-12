def main():
    def fun(n: int):
        one = 9
        n -= 9
        if n <= 0:
            oneStack.append(n + 9)
            return
        oneStack.append(one)
        two = int(str(n)[-1])
        n -= two
        twoStack.append(two)
        fun(n // 10)

    oneStack = []
    twoStack = []
    fun(int(input().strip()))
    print(sum(oneStack) + sum(twoStack))


for _ in range(int(input().strip())):
    main()
