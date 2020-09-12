def main():
    def takeAt(slotIdx: int):
        """
        取第slotIdx个槽的东西，返回物品的id（slotIdx是1-based）
        """
        ret = slots[slotIdx - 1].pop()
        if not slots[slotIdx - 1]:  # 如果空了自动续槽
            slots[slotIdx - 1].append(slotIdx)
        return ret

    def returnAt(slotIdx: int, elementId: int):
        slots[slotIdx - 1].append(elementId)

    slotCount, peopleCount = list(map(int, input().strip().split()))  # 槽的数量，人的数量
    elementId2Price = [-1] + list(map(int, input().strip().split()))[:slotCount]  # 槽对应物品的单价
    slots = [[elemId] for elemId in range(1, slotCount + 1)]  # 初始化各个槽。每个槽里的物品id等于这个槽
    for _ in range(peopleCount):  # 每个人
        operationCount = int(input().strip())  # 操作总次数
        leftHandId, rightHandId = -1, -1  # 左右手拿的是哪个物品
        keepIds = []
        for _ in range(operationCount):
            inputWords = input().strip().split()
            # 前提条件
            assert len(inputWords) == 2 or (len(inputWords) == 3 and inputWords[2].isdigit())
            assert inputWords[0] in ['left', 'right']
            assert inputWords[1] in ['take', 'return', 'keep']
            # 拿出物品
            if inputWords[1] == 'take':
                slotIdx = int(inputWords[2])  # 要取出哪个槽的东西
                if inputWords[0] == 'left':
                    assert leftHandId == -1  # 前提条件，手里没有东西
                    leftHandId = takeAt(slotIdx)  # 从槽里拿出一个东西
                elif inputWords[0] == 'right':
                    assert rightHandId == -1
                    rightHandId = takeAt(slotIdx)
            # 还回物品
            elif inputWords[1] == 'return':
                slotIdx = int(inputWords[2])  # 要还回哪个槽的东西
                if inputWords[0] == 'left':
                    assert leftHandId != -1
                    returnAt(slotIdx, leftHandId)
                    leftHandId = -1
                elif inputWords[0] == 'right':
                    assert rightHandId != -1
                    returnAt(slotIdx, rightHandId)
                    rightHandId = -1
            # 放进背包
            elif inputWords[1] == 'keep':
                if inputWords[0] == 'left':
                    keepIds.append(leftHandId)
                    leftHandId = -1
                elif inputWords[0] == 'right':
                    keepIds.append(rightHandId)
                    rightHandId = -1
        # 手里还拿着东西，自动放进包里
        if leftHandId != -1:
            keepIds.append(leftHandId)
        if rightHandId != -1:
            keepIds.append(rightHandId)
        totalMoney = 0
        for elementId in keepIds:
            totalMoney += elementId2Price[elementId]
        print(totalMoney)


main()


# region Test
def testIt():
    strings = '5 3\n' + \
              '1 2 3 4 5\n' + \
              '5\n' + \
              'left take 1\n' + \
              'right take 2\n' + \
              'left return 3\n' + \
              'right keep\n' + \
              'right take 4\n' + \
              '6\n' + \
              'left take 5\n' + \
              'right take 1\n' + \
              'left return 2\n' + \
              'right return 3\n' + \
              'left take 5\n' + \
              'left return 4\n' + \
              '10\n' + \
              'left take 1\n' + \
              'left keep\n' + \
              'left take 2\n' + \
              'left keep\n' + \
              'left take 3\n' + \
              'left keep\n' + \
              'left take 4\n' + \
              'left keep\n' + \
              'left take 5\n' + \
              'left keep'
    strings = strings.split('\n')
    for s in strings:
        yield str(s)


g = testIt()


def input():
    return next(g)
# endregion
