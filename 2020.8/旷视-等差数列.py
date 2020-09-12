import sys


def _input():
    return sys.stdin.readline()


while True:
    N = int(_input().strip())
    array = list(map(int, _input().strip().split()))[:N]
    array.sort()
    magicNums = 0
    while array and array[magicNums] == 0:
        magicNums += 1
    i = magicNums + 1
    while i < len(array):
        if array[i] == array[i - 1]:
            break
        if array[i] - array[i - 1] > 1:
            need = array[i] - array[i - 1] - 1
            if magicNums >= need:
                magicNums -= need
            else:
                break
        i += 1
    else:
        print('Valid')
        continue
    print('Invalid')
