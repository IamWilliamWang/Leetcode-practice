from collections import defaultdict

# 每次找出叶子节点(id2ChildrenCount[i]==0)，在relationIds找叶子节点父亲是哪个，找到后记录{叶子:父亲}，并删除该节点(id2ChildrenCount[父亲]-=1，relationIds删除)
def get叶子s():
    for i in range(1, len(list第i个人有多少个孩子)):
        if i in dict孩子to爸爸的Id:  # 孩子死了
            continue
        if list第i个人有多少个孩子[i] == 0:  # 没有死，没有孩子
            yield i


def get父子关系Tuple(id):
    for tpl in list所有关系元组:
        if id in tpl:
            return tpl
    return None


n人数 = int(input().strip())
list所有关系元组 = []
for _ in range(n人数 - 1):
    list所有关系元组.append(tuple(map(int, input().strip().split())))
list第i个人有多少个孩子 = [0] + list(map(int, input().strip().split()))
dict孩子to爸爸的Id = defaultdict(int)

while any(list第i个人有多少个孩子[1:]):
    for id没孩子的人 in get叶子s():
        tuple父子关系 = get父子关系Tuple(id没孩子的人)
        id父亲 = list(tuple父子关系)
        id父亲.remove(id没孩子的人)
        id父亲 = id父亲[0]
        dict孩子to爸爸的Id[id没孩子的人] = id父亲  # 记录
        list第i个人有多少个孩子[id父亲] -= 1  # 删除叶子节点，断绝关系
        list所有关系元组.remove(tuple父子关系)  # 删除叶子节点的所有关系

query = int(input().strip())
for _ in range(query):
    id1, id2 = list(map(int, input().strip().split()))
    ancestor1List = [id1]
    ancestor2List = [id2]
    while dict孩子to爸爸的Id[ancestor1List[-1]] != 0:
        ancestor1List.append(dict孩子to爸爸的Id[ancestor1List[-1]])
        if ancestor1List[-1] == id2:
            print('SSSS')
            break
    else:
        while dict孩子to爸爸的Id[ancestor2List[-1]] != 0:
            ancestor2List.append(dict孩子to爸爸的Id[ancestor2List[-1]])
            if ancestor2List[-1] == id1:
                print('ZZZZ')
                break
        else:
            if len(ancestor1List) > len(ancestor2List):
                ancestor1List, ancestor2List = ancestor2List, ancestor1List
            for x in ancestor1List:
                if x in ancestor2List:
                    print(x)
                    break
