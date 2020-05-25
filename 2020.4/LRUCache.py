class Cache:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value


class LRUCache:

    def __init__(self, capacity: int):
        self.cacheList = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        foundList = list(filter(lambda element: element.key == key, self.cacheList))
        if not foundList:
            return -1
        cacheBlock = foundList[0]
        self.cacheList.remove(cacheBlock)
        self.cacheList.append(cacheBlock)
        return cacheBlock.value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        foundList = list(filter(lambda element: element.key == key, self.cacheList))
        if foundList:
            cacheBlock = foundList[0]
            cacheBlock.value = value
            self.cacheList.remove(cacheBlock)
            self.cacheList.append(cacheBlock)
        else:
            if len(self.cacheList) >= self.capacity:
                self.cacheList.pop(0)
            newCache = Cache(key=key, value=value)
            self.cacheList.append(newCache)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
cache = LRUCache(2)

print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))  # 返回 1
print(cache.put(3, 3))  # 去除 key 2
print(cache.get(2))  # 返回 -1 (未找到key 2)
print(cache.get(3))  # 返回 3
print(cache.put(4, 4))  # 去除 key 1
print(cache.get(1))  # 返回 -1 (未找到 key 1)
print(cache.get(3))  # 返回 3
print(cache.get(4))  # 返回 4
