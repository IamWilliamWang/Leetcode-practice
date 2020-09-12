n = int(input().strip())
arr = set(map(int, input().strip().split()))
m = int(input().strip())
output = []
for num in (map(int, input().strip().split())):
    if num in arr:
        output.append(num)
print(' '.join(map(str, output)))
