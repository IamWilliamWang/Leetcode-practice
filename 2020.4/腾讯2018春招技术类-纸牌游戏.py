import sys

n = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().strip().split()))
cards.sort(reverse=True)
result = 0
for i in range(n):
    if i % 2 == 0:
        result += cards[i]
    else:
        result -= cards[i]
print(result)
