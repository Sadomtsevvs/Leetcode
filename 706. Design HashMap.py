class ListNode:

    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:

    def __init__(self):
        self.m = dict()

    def put(self, key: int, value: int) -> None:
        pos = key % 1000
        if pos not in self.m:
            self.m[pos] = ListNode(key, value)
        else:
            cur = self.m[pos]
            prev = ListNode(0, 0, cur)
            while cur:
                if cur.key == key:
                    cur.value = value
                    return
                prev, cur = cur, cur.next
            prev.next = ListNode(key, value)

    def get(self, key: int) -> int:
        pos = key % 1000
        if pos in self.m:
            cur = self.m[pos]
            while cur:
                if cur.key == key:
                    return cur.value
                cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        pos = key % 1000
        if pos not in self.m:
            return
        if self.m[pos].key == key:
            self.m[pos] = self.m[pos].next
            if self.m[pos] is None:
                del self.m[pos]
        else:
            prev = self.m[pos]
            cur = prev.next
            while cur:
                if cur.key == key:
                    prev.next = cur.next
                    return
                prev, cur = cur, cur.next

# class MyHashMap:
#
#     def __init__(self):
#         self.d = [-1] * (10**6 + 1)
#
#     def put(self, key: int, value: int) -> None:
#         self.d[key] = value
#
#     def get(self, key: int) -> int:
#         return self.d[key]
#
#     def remove(self, key: int) -> None:
#         self.d[key] = -1

# solution from LC comments
#
# # using just arrays, direct access table
# # using linked list for chaining
#
# class ListNode:
#     def __init__(self, key, val):
#         self.pair = (key, val)
#         self.next = None
#
#
# class MyHashMap:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.m = 1000;
#         self.h = [None] * self.m
#
#     def put(self, key, value):
#         """
#         value will always be non-negative.
#         :type key: int
#         :type value: int
#         :rtype: void
#         """
#         index = key % self.m
#         if self.h[index] == None:
#             self.h[index] = ListNode(key, value)
#         else:
#             cur = self.h[index]
#             while True:
#                 if cur.pair[0] == key:
#                     cur.pair = (key, value)  # update
#                     return
#                 if cur.next == None: break
#                 cur = cur.next
#             cur.next = ListNode(key, value)
#
#     def get(self, key):
#         """
#         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
#         :type key: int
#         :rtype: int
#         """
#         index = key % self.m
#         cur = self.h[index]
#         while cur:
#             if cur.pair[0] == key:
#                 return cur.pair[1]
#             else:
#                 cur = cur.next
#         return -1
#
#     def remove(self, key):
#         """
#         Removes the mapping of the specified value key if this map contains a mapping for the key
#         :type key: int
#         :rtype: void
#         """
#         index = key % self.m
#         cur = prev = self.h[index]
#         if not cur: return
#         if cur.pair[0] == key:
#             self.h[index] = cur.next
#         else:
#             cur = cur.next
#             while cur:
#                 if cur.pair[0] == key:
#                     prev.next = cur.next
#                     break
#                 else:
#                     cur, prev = cur.next, prev.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


myHashMap = MyHashMap()
myHashMap.put(1, 1) # The map is now [[1,1]]
myHashMap.put(2, 2) # The map is now [[1,1], [2,2]]
print(myHashMap.get(1))    # return 1, The map is now [[1,1], [2,2]]
print(myHashMap.get(3))    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1) # The map is now [[1,1], [2,1]] (i.e., update the existing value)
print(myHashMap.get(2))    # return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2) # remove the mapping for 2, The map is now [[1,1]]
print(myHashMap.get(2))    # return -1 (i.e., not found), The map is now [[1,1]]