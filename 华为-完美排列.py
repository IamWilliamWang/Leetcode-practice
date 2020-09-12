def main():
    bestN = int(input().strip())
    bestShape = list(map(int, input().strip().split()))[:bestN]
    bestValue = list(map(int, input().strip().split()))[:bestN]
    bests = [(shape, value) for shape, value in zip(bestShape, bestValue)]

    N = int(input().strip())
    shapes = list(map(int, input().strip().split()))[:N]
    values = list(map(int, input().strip().split()))[:N]
    goods = [(shape, value) for shape, value in zip(shapes, values)]

    goodsStr = str(goods)[1:-1]
    idx = goodsStr.find(str(bests)[1:-1])
    if idx == -1:
        print(0)
        return
    print(goodsStr[:idx + 1].count('('))


main()
