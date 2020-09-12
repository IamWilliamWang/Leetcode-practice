def dictionary(nowStr: str, a_count: int, b_count: int):
    global N, M, K, wordCounter
    if a_count > N or b_count > M:
        return
    if nowStr:
        wordCounter += 1
        # print(nowStr)
        if wordCounter == K:
            print(nowStr)
            exit(0)
    dictionary(nowStr + 'a', a_count + 1, b_count)
    dictionary(nowStr + 'b', a_count, b_count + 1)


N, M, K = list(map(int, input().strip().split()))
wordCounter = 0
dictionary('', 0, 0)
