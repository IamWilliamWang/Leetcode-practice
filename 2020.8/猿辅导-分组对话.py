import sys

count = int(input().strip())
for _ in range(count):
    arr = sorted(map(int, input().strip().split()))[1:]
    while arr and arr[0] == 0:
        arr.pop(0)
    if len(arr) < 3:
        sys.stdout.write('0')
    sys.stdout.write(str(arr[0]))
