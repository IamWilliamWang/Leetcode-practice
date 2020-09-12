inStr = input().strip()
SPLITS = [ch for ch in '+-*/%&|^<>={}()']
output = ['']
for ch in inStr:
    if ch == ' ':
        continue
    if ch in SPLITS:
        output.append(ch)
        output.append('')
    else:
        output[-1] = output[-1] + ch
if output[0] == '':
    output.pop(0)
output = ' '.join(output)
if output[-1] not in ',;':
    output = output + ' '
if output[0] == ' ' and output[1:2] in '({':
    output = output[1:]
if output[-1] == ' ' and output[-2:-1] in '({':
    output = output[:-1]
print(output)
