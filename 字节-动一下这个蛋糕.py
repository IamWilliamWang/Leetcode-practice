row, col = list(map(int, input().strip().split()))
if (row * col) % 2 != 0:
    print(0)
    exit(0)
if row % 2 == 1:
    row, col = col, row
fi = [0, 1, 2]
for i in range(3, row + 1):
    fi.append(fi[-1] + fi[-2])
fi = [0, row // 2, fi[row]]
for i in range(3, col + 1):
    fi.append(fi[-1] + fi[-2])
print(fi[col])
