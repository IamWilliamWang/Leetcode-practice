mealCount, orderCount = list(map(int, input().strip().split()))
menuDict = {}
for _ in range(mealCount):
    key, value = input().strip().split()
    menuDict[key] = int(value)
originalMenu = menuDict.copy()

orderedPeople = set()
for _ in range(orderCount):
    name, orderType, element = input().strip().split()
    if element not in menuDict:
        print('no')
    elif orderType == 'release':
        if name in orderedPeople and menuDict[element] < originalMenu[element]:
            menuDict[element] += 1
            orderedPeople.remove(name)
            print('yes')
        else:
            print('no')
    elif menuDict[element] == 0:
        print('no')
    else:
        menuDict[element] -= 1
        orderedPeople.add(name)
        print('yes')
