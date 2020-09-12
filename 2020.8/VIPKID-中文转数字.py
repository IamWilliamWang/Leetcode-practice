from itertools import chain


def main():
    result = []  # 全部小区间组成完整数字
    stack = [0] * 4  # 小区间
    big分割位 = ['万', '亿']
    small分割位 = {ch: i + 1 for i, ch in enumerate('十百千')}
    digits = {ch: i + 1 for i, ch in enumerate('一二三四五六七八九')}

    def refresh():
        nonlocal stack, p, format
        result.append(stack)
        stack = [0] * 4
        p = 0
        format = True

    def stackPeekNonZero(stacksize: int):
        tmp = stack[:stacksize]
        while tmp and tmp[-1] == 0:
            tmp.insert(0, tmp.pop())
        stack[:stacksize] = tmp

    p = 0  # 当前写入位
    format = True  # 小区间进行数字跃进，13000 -> 00013
    for ch in reversed(input().strip()):
        if ch in digits:
            stack[p] = digits[ch]
            p += 1
        elif ch in small分割位:
            if not format:
                p = small分割位[ch]
            else:
                if small分割位[ch] - p > 1:
                    stackPeekNonZero(small分割位[ch])
            stack[p] = 1
        elif ch in big分割位:
            if format:
                tmp = stack
                while tmp and tmp[-1] == 0:
                    tmp.insert(0, tmp.pop())
                stack = tmp
            if ch == '亿' and not result:
                refresh()
                refresh()
            else:
                refresh()
        elif ch == '零':
            format = False
    if stack:
        while stack and stack[-1] == 0:
            stack.pop()
        refresh()

    print(''.join(map(str, chain(*result)))[::-1])


main()
# 编写一个算法把中文的字符串转换成整数，不用考虑long的溢出问题，假设它可以存储任意大的整数。 long parseChineseNumber(string s); 测试用例： 1. "一千零一" -> 1001 2. "一千零一万五千四百三十二亿九千八百七十六万四千三百零二" -> 1001543298764302 3. "十五" -> 15 4. "五万三" -> 53000 5. "四万亿" -> 4000000000000
