def parse(l: list) -> str:
    result = ''
    for ch in l:
        result += ch
    return result

def fun(input: list):
    hasDict = dict()
    output = []
    for itemList in input:
        comparableList = itemList.copy()
        comparableList.sort()
        if parse(comparableList) not in hasDict:
            hasDict[parse(comparableList)] = len(output)
            output.append([comparableList])
        else:
            output[hasDict[parse(comparableList)]].append(itemList)
    return output

input = [
    ['1', '2', '3'], ['3', '2', '1'], ['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'c', 'a'], ['c', 'b', 'a'], ['a', 'b'],
    ['b', 'a']
]
print(fun(input))
