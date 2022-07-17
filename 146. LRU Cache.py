class Node:

    def __init__(self, key=-1, value=-1, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.hext = self.tail
        self.tail.prev = self.head

    def update_key(self, key):
        # we need to move key to the tail, except it is already the last
        if self.cache[key] == self.tail.prev:
            return self.cache[key].value
        # connect adjacent nodes after deleting node
        self.cache[key].prev.next = self.cache[key].next
        self.cache[key].next.prev = self.cache[key].prev
        # put node to the tail
        self.tail.prev.next, self.cache[key].prev = self.cache[key], self.tail.prev
        self.tail.prev, self.cache[key].next = self.cache[key], self.tail

    def get(self, key: int) -> int:
        if key in self.cache:
            self.update_key(key)
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.update_key(key)
            self.cache[key].value = value
        else:
            # add to the tail
            node = Node(key, value, self.tail.prev, self.tail)
            self.tail.prev.next = node
            self.tail.prev = node
            if self.head.next == self.tail:
                self.head.next = node
            # add to the cache
            self.cache[key] = node
            # if cache is full, delete first from the head
            if len(self.cache) > self.capacity:
                key_to_delete = self.head.next.key
                self.head.next = self.cache[key_to_delete].next
                self.cache[key_to_delete].next.prev = self.head
                del self.cache[key_to_delete]


    # first approach, it is not O(1) for put
    #
    # def __init__(self, capacity: int):
    #     self.capacity = capacity
    #     self.cache = {}
    #     self.pos = {}
    #     self.mn = -1
    #     self.mx = -1
    #
    # def update_key(self, key):
    #     pos = self.cache[key][1]
    #     self.mx += 1
    #     self.cache[key][1] = self.mx
    #     self.pos[self.mx] = key
    #     del self.pos[pos]
    #
    # def get(self, key: int) -> int:
    #     if key in self.cache:
    #         self.update_key(key)
    #         return self.cache[key][0]
    #     else:
    #         return -1
    #
    # def put(self, key: int, value: int) -> None:
    #     if key in self.cache:
    #         self.update_key(key)
    #     elif len(self.cache) == self.capacity:
    #         while self.mn not in self.pos:
    #             self.mn += 1
    #         del self.cache[self.pos[self.mn]]
    #         del self.pos[self.mn]
    #     self.mx += 1
    #     self.cache[key] = [value, self.mx]
    #     self.pos[self.mx] = key


LRUCache = LRUCache(2)
LRUCache.put(1, 1)
LRUCache.put(2, 2)
print(LRUCache.get(1))
LRUCache.put(3, 3)
print(LRUCache.get(2))
LRUCache.put(4, 4)
print(LRUCache.get(1))
print(LRUCache.get(3))
print(LRUCache.get(4))