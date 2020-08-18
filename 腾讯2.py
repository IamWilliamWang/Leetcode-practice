def minus(num1: str, num2: str, positionBegin=None) -> str:
    num1 = [int(ch) for ch in num1]
    num2 = [int(ch) for ch in num2]
    j = len(num2) - 1
    if positionBegin is None:
        i = len(num1) - 1
    else:
        i = positionBegin + len(num2) - 1
    while i >= 0 and j >= 0:
        num1[i] -= num2[j]
        if i != 0 and num1[i] < 0:
            num1[i] += 10
            num1[i - 1] -= 1
        i -= 1
        j -= 1
    return ''.join(map(str, num1))


def divide(num1: str, num2: str, n: int) -> str:
    # return float(num1) / float(num2)
    dividingNumber = num1 + '0' * n
    resultInt, resultDot = [], []
    for divideAt in range(len(dividingNumber) - len(num2) + 1):
        minusTimes = 0
        while True:
            ans = minus(dividingNumber, num2, divideAt)
            if '-' in ans:
                break
            dividingNumber = ans
            minusTimes += 1
        if divideAt + len(num2) > len(num1):  # 小数部分
            resultDot.append(minusTimes)
        else:
            resultInt.append(minusTimes)
    result = ''.join([str(x) for x in resultInt])
    if resultDot:
        result += '.' + ''.join([str(x) for x in resultDot])
    nonZeroStartIdx = 0
    while nonZeroStartIdx < len(result) and result[nonZeroStartIdx] == '0':
        nonZeroStartIdx += 1
        if result[nonZeroStartIdx] == '.':
            nonZeroStartIdx -= 1
            break
    if len(resultInt) < n:  # 整数不够用
        ans = result[nonZeroStartIdx:nonZeroStartIdx + n + 1]
    else:
        ans = result[nonZeroStartIdx:nonZeroStartIdx + n]
    if len(ans) < len(num1):  # 补0
        ans += '0' * (len(num1) - len(ans) - 1)
    return ans


print(divide('123456789123456789123456789', '100000000000000', 5))
