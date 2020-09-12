def main():
    def contains(fatherI: int, childI: int):
        return sections[fatherI][0] <= sections[childI][0] and sections[fatherI][1] >= sections[childI][1]

    n = int(input().strip())
    sections = []
    for _ in range(n):
        sections.append(tuple(map(int, input().strip().split())))
    sections.sort()
    orders = []  # 任务时间、是否开始、任务id
    for i, section in enumerate(sections):
        orders += [(section[0], True, i), (section[1], False, i)]
    orders.sort()  # 时间升序，先关后开
    adjMap = {}
    array = []  # 开始时间、任务id
    for orderTime, isOpen, orderId in orders:
        if not isOpen:
            array.remove([a for a in array if a[1] == orderId][0])  # 关掉这个区间
        else:
            adjMap[orderId] = [a[1] for a in array]
            array += [(orderTime, orderId)]
    for node in adjMap:
        nextNodes = adjMap[node]
        ignores = set()
        for nextNode in nextNodes:
            if contains(node, nextNode) or contains(nextNode, node):
                ignores.add(nextNode)
        adjMap[node] = [nextNode for nextNode in nextNodes if nextNode not in ignores]
    for node in adjMap:
        for nextNode in adjMap[node]:
            if node not in adjMap[nextNode]:
                adjMap[nextNode].append(node)
    visited = set()

    def dfs(i: int):
        if i in visited:
            return
        visited.add(i)
        for nextNode in adjMap[i]:
            dfs(nextNode)

    dfs(0)
    if len(visited) != n:
        print('NO')
        return

    def 拓扑():
        while len(adjMap) > 0:
            singleNodes = []
            for node in adjMap:
                if len(adjMap[node]) == 0:
                    return False
                if len(adjMap[node]) == 1:
                    singleNodes += [node]
            if not singleNodes:
                return False
            for single in singleNodes:
                del adjMap[single]
            ignores = set()
            for node in adjMap:
                adjMap[node] = sorted(set(adjMap[node]).difference(singleNodes))
                if not adjMap[node]:
                    ignores.add(node)
            for i in ignores:
                del adjMap[i]
        return True

    print('YES' if 拓扑() else 'NO')


for _ in range(int(input().strip())):
    main()
