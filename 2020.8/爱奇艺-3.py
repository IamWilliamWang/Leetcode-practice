def convert(endCh: str):
    return '{[('['}])'.index(endCh)]


stack = []
for ch in input().strip():
    if ch not in '([{}])':
        print('False')
        exit(0)
    if ch in '([{':
        stack.append(ch)
    else:
        if not stack or stack[-1] != convert(ch):
            print('False')
            exit(0)
        stack.pop()
print('False' if stack else 'True')
