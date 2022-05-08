# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):

        def flatten(fl, nl):
            for el in reversed(nl):
                if el.isInteger():
                    fl.append(el.getInteger())
                else:
                    flatten(fl, el.getList())

        self.flatten = []
        flatten(self.flatten, nestedList)

    def next(self) -> int:
        return self.flatten.pop()

    def hasNext(self) -> bool:
        return self.flatten

# from LC comments, nice, but i don't like reversing list in init
#
# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         self.stack = nestedList[::-1]
#
#     def next(self) -> int:
#         return self.stack.pop().getInteger()
#
#     def hasNext(self) -> bool:
#         while self.stack:
#             if self.stack[-1].isInteger():
#                 return True
#             self.stack.extend(self.stack.pop().getList()[::-1])
#         return False

# another LC solution
#
# class NestedIterator(object):
#
#     def __init__(self, nestedList):
#         def gen(nestedList):
#             for x in nestedList:
#                 if x.isInteger():
#                     yield x.getInteger()
#                 else:
#                     for y in gen(x.getList()):
#                         yield y
#         self.gen = gen(nestedList)
#
#     def next(self):
#         return self.value
#
#     def hasNext(self):
#         try:
#             self.value = next(self.gen)
#             return True
#         except StopIteration:
#             return False

class NestedIterator:

    def __init__(self, nestedList):
        def gen(nestedList):
            for x in nestedList:
                if x.isInteger():
                    yield x.getInteger()
                else:
                    for y in gen(x.getList()):
                        yield y
        self.gen = gen(nestedList)
        self.value = None
        self.next()

    def next(self):
        value = self.value
        try:
            self.value = self.gen
            self.has_next = True
        except StopIteration:
            self.has_next = False
        return value

    def hasNext(self):
        return self.has_next


    # Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())