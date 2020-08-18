def _input():
    import sys
    return sys.stdin.readline()


a, b = list(map(int, _input().strip().split()))
count = 0
for x in range(b, a + 1):
    if a % x == b:
        count += 1
print(count if count else 'inf')
