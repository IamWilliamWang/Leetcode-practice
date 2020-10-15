def getLargestRectangle(heights: list) -> int:
    if not heights:
        return 0
    indexStack = []  # 每次能保证[heights[i] for i in stack]为升序
    chainLeft = []  # 搜索每一点之前的，最后一个小于该height的index。结构仿佛像链表一样的
    chainRight = []  # 搜索每之后的第一个小于该height的index。范围[left+1,right-1]即为以当前为高度为高的最长宽
    # 由左到右来一遍，记录chainLeft
    for now_i, height in enumerate(heights):
        while indexStack and heights[indexStack[-1]] >= height:  # 弹出所有比现在高的节点，因为不会阻挡向左延伸
            indexStack.pop()
        chainLeft.append(indexStack[-1] if indexStack else -1)  # 如果栈为空，说明左边能一直延伸，置为-1
        indexStack.append(now_i)  # 当前节点入栈
    indexStack = []  # 清空栈
    # 由右向左来一遍，记录chainRight
    for now_i in range(len(heights) - 1, -1, -1):
        while indexStack and heights[indexStack[-1]] >= heights[now_i]:  # 弹出所有比现在高的节点，因为不会阻挡向右延伸
            indexStack.pop()
        chainRight.append(indexStack[-1] if indexStack else len(heights))  # 如果栈为空，说明右边能一直延伸
        indexStack.append(now_i)
    assert len(chainLeft) == len(chainRight) == len(heights)
    # 开始算最大长方形面积
    maxArea = []
    # 使用每个对应点的左、右边界(exclusive)和当前高度，计算面积。注意：chainRight需要逆序再使用
    for left, right, now_height in zip(chainLeft, reversed(chainRight), heights):
        maxArea.append((right - (left + 1)) * now_height)
    return max(maxArea)


N = int(input().strip())
array = list(map(int, input().strip().split()))
result = getLargestRectangle(array)
print(result)
