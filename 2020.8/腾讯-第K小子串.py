def main():
    INF = 2 ** 15 - 1
    maxLen = [0] * (INF * 2)
    trans = [[0] * (INF * 2) for _ in range(30)]
    link, x, y, cnt = [0] * (INF * 2), [0] * (INF * 2), [0] * (INF * 2), [0] * (INF * 2)
    num, last = 0, 0
    sums = [0] * (INF * 2)

    def init():
        nonlocal num, last
        num = last = 1
        maxLen[last] = link[last] = 0

    def insert(_id: int):
        nonlocal num, last
        num += 1
        z = num
        maxLen[z] = maxLen[last] + 1
        p = last
        while p and not trans[p][_id]:
            trans[p][_id] = z
            p = link[p]
        if not p:
            link[z] = 1
        else:
            _x = trans[p][_id]
            if maxLen[_x] == maxLen[p] + 1:
                link[z] = _x
            else:
                num += 1
                maxLen[num] = maxLen[p] + 1
                trans[num] = trans[_x].copy()
                link[num] = link[_x]
                while p and trans[p][_id] == _x:
                    trans[p][_id] = num
                    p = link[p]
                link[_x] = link[z] = num
        last = z
        cnt[z] = 1

    def count():
        for i in range(1, num + 1):
            x[maxLen[i]] += 1
        for i in range(1, num + 1):
            x[i] += x[i - 1]
        for i in range(1, num + 1):
            y[x[maxLen[i]]] = i
            x[maxLen[i]] -= 1
        for i in range(num, 0, -1):
            cnt[link[y[i]]] += cnt[y[i]]

    def calSum():
        for i in range(num, 0, -1):
            sums[y[i]] = 1
            for j in range(26):
                sums[y[i]] += sums[trans[y[i]][j]]

    def getKth(k: int):
        cur, nxt = 1, 0
        ans = ''
        while k:
            for i in range(26):
                if trans[cur][i] and k:
                    nxt = trans[cur][i]
                    if k > sums[nxt]:
                        k -= sums[nxt]
                    else:
                        k -= 1
                        cur = nxt
                        ans += chr(ord('a') + i)
                        break
        return ans

    string = input().strip()
    k = int(input().strip())
    init()
    for _i in range(len(string)):
        insert(ord(string[_i]) - ord('a'))
    count()
    calSum()
    print(getKth(k))


main()
