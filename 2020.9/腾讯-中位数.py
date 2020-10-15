n = int(input().strip())
array = list(map(int, input().strip().split()))
array = [(num, i) for i, num in enumerate(array)]
array.sort()
output = {}
specialPoints = [len(array) // 2] if len(array) % 2 else []
for i in range(len(array)):
    if len(array) % 2 == 1 and i == len(array) // 2:
        output[array[i][1]] = (array[len(array) // 2 - 1][0] + array[len(array) // 2 + 1][0]) / 2
        continue
    addOffset = i < len(array) / 2
    if len(array) % 2 == 0:  # 新数组是奇数个
        midIndex = (len(array) - 1) // 2 + int(addOffset)
        output[array[i][1]] = array[midIndex][0]
    else:  # 新数组是偶数个
        midIndex = len(array) // 2
        midIndex = midIndex - 1 + int(addOffset), midIndex + int(addOffset)
        output[array[i][1]] = (array[midIndex[0]][0] + array[midIndex[1]][0]) / 2
for key in sorted(output.keys()):
    midNumber = output[key]
    if int(midNumber) == midNumber:
        midNumber = int(midNumber)
    print(midNumber)
