from typing import List

def product(*args):
    result = [[]]
    for pool in args:
        result = [x + [y] for x in result for y in pool]
    return result

def permutations(array: List[List[str]]) -> str:
    def getElements() -> str:  # 每次返回一个全排列的字符串之一
        for series in product(*array):
            yield ''.join(series)  # 各取一个进行拼接

    return ','.join(getElements())


print(permutations([['A', 'B', 'C'], ['D', 'E'], ['F', 'G']]))
