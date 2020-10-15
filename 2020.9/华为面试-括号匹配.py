def main():
    inStr = input().strip()
    signalStack = []
    lefts = '{[('
    rights = '}])'
    valid = True
    for ch in inStr:
        if ch in lefts:  # 左括号
            signalStack.append(ch)
        elif ch in rights:  # 右括号
            if not signalStack or signalStack[-1] != lefts[rights.index(ch)]:  # stack为空或者栈顶不对
                valid = False
                break
            signalStack.pop()  # 出栈
        else:  # 其他字符
            pass
    if valid:
        valid = (len(signalStack) == 0)
    return valid


print(main())
