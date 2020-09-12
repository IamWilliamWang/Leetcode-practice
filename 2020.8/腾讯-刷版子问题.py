def main():
    N = int(input().strip())
    array = list(map(int, input().strip().split()))[:N]
    result = 2 ** 31

    def brush(restArray: list, brushCount: int):
        nonlocal result
        if not any(restArray):
            result = min(result, brushCount)
            return
        non0Idx = 0
        while not restArray[non0Idx]:
            non0Idx += 1
        # 横着刷一道，从前刷到后
        array = restArray.copy()
        i = non0Idx
        while i < len(array) and array[i]:
            array[i] -= 1
            i += 1
        if i - non0Idx > restArray[non0Idx]:
            brush(array, brushCount + 1)
        else:
            # 竖着刷一道
            array = restArray.copy()
            array[non0Idx] = 0
            brush(array, brushCount + 1)

    brush(array, 0)
    print(result)


main()
