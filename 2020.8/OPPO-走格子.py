from functools import reduce


def main():
    def ok(i: int, j: int):
        return 0 <= i < rows and 0 <= j < cols and (i, j) not in visited and reduce(lambda a, b: int(a) + int(b),
                                                                                    str(i) + str(j)) <= limit

    rows, cols, limit = list(map(int, input().strip().split()))
    queue = [(0, 0)]
    result = 0
    visited = set()
    while queue:
        x, y = queue.pop(0)
        if not ok(x, y):
            continue
        visited.add((x, y))
        result += 1
        queue += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    print(result)


for _ in range(int(input())):
    main()
