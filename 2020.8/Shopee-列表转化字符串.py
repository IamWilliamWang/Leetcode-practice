def toString(l: list) -> list:
    chars = []
    for element in l:
        if type(element) == str:
            chars.append(element)
        elif type(element) == list:
            chars += toString(element)
        else:
            raise ValueError
    return chars


print('"' + '\\n'.join(toString(eval(input().strip()))) + '"')
