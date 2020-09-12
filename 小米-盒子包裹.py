n = int(input().strip())
array = list(map(int, input().strip().split()))
array.sort(reverse=True)
result = 0
while array:  # array储存未被打包到数
    i = 1
    nowNum = array[0]
    delNums = [nowNum]
    while i < len(array):
        if array[i] < delNums[-1]:
            delNums.append(array[i])
        i += 1
    # 统计并打包
    result += 1
    for x in delNums:
        array.remove(x)
print(result)
