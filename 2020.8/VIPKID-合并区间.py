N = int(input().strip())
sections = []
for _ in range(N):
    sections.append(list(map(int, input().strip().split())))
orders = []
for section in sections:
    orders += [(section[0], False), (section[1], True)]
orders.sort()
now = 0
result = []
for order in orders:
    if order[1]:
        now -= 1
        if now == 0:
            end = order[0]
            result += [(start, end)]
    else:
        now += 1
        if now == 1:
            start = order[0]
for line in result:
    print(line[0], line[1])
