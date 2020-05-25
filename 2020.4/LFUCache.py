from functools import cmp_to_key

globalClock = 0  # 总时钟


def clockTime():
    global globalClock
    nowClockTime = globalClock
    globalClock += 1
    return nowClockTime


class Cache:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.visit_freq = 1
        self.clock = clockTime()


# def compareCache(cache1: Cache, cache2: Cache):
#     if cache1.visit_freq == cache2.visit_freq: # 如果访问频率相同，则时钟越大的，越靠前
#         return cache2.clock - cache1.clock
#     return cache1.visit_freq - cache2.visit_freq # 访问频率越小的越靠前


class LFUCache:

    def __init__(self, capacity: int):
        self.cacheList = []
        self.capacity = capacity

    def sortWithLFU(self) -> None:
        self.cacheList.sort(key=cmp_to_key(
            lambda cache1, cache2: cache1.clock - cache2.clock if cache1.visit_freq == cache2.visit_freq else cache1.visit_freq - cache2.visit_freq))

    def get(self, key: int) -> int:
        foundList = list(filter(lambda element: element.key == key, self.cacheList))
        if not foundList:
            return -1
        cacheBlock = foundList[0]
        cacheBlock.visit_freq += 1
        cacheBlock.clock = clockTime()
        self.sortWithLFU()
        return cacheBlock.value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        foundList = list(filter(lambda element: element.key == key, self.cacheList))
        if foundList:
            cacheBlock = foundList[0]
            cacheBlock.value = value
            cacheBlock.visit_freq += 1
            cacheBlock.clock = clockTime()
        else:
            if len(self.cacheList) >= self.capacity:
                self.cacheList.pop(0)
            newCache = Cache(key=key, value=value)
            self.cacheList.append(newCache)
        self.sortWithLFU()





# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
cache = LFUCache(2)

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
