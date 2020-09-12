n = int(input().strip())
arr = [1]
index = [0, 0, 0]
for _ in range(n - 1):
    arr.append(min(arr[index[0]] * 2, arr[index[1]] * 3, arr[index[2]] * 5))
    if arr[index[0]] * 2 == arr[-1]:
        index[0] += 1
    if arr[index[1]] * 3 == arr[-1]:
        index[1] += 1
    if arr[index[2]] * 5 == arr[-1]:
        index[2] += 1
print(arr[n - 1])
