def get(n):
    if n < 5:
        return 0
    n = n // 5
    return n + get(n)


print(get(int(input().strip())))
