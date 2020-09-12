n = int(input().strip())
data = []
for _ in range(n):
    a, b = list(map(int, input().strip().split()))
    data += [(a, b)]
data.sort(key=lambda t: (t[1], -t[0]))
nowScore = 0
while data and data[0][1] == 0:
    nowScore += data[0][0]
    del data[0]
for score, treasure in data:
    if treasure and nowScore * 2 > nowScore + score:
        nowScore *= 2
    else:
        nowScore += score
print(nowScore)
