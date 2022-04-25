# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator():
    def __init__(self, iterator):
        self.iter = iterator
        self.prev_hasNext = self.iter.hasNext()
        self.prev_peek = self.iter.next()


    def peek(self):
        return self.prev_peek

    def next(self):
        ans = self.prev_peek
        if self.iter.hasNext():
            self.prev_peek = self.iter.next()
        else:
            self.prev_hasNext = False
        return ans

    def hasNext(self):
        return self.prev_hasNext

# solution from Babichev
#
# class PeekingIterator:
#     def __init__(self, iterator):
#         self.iterator = iterator
#         self.buffer = self.iterator.next() if self.iterator.hasNext() else None
#
#     def peek(self):
#         return self.buffer
#
#     def next(self):
#         tmp = self.buffer
#         self.buffer = self.iterator.next() if self.iterator.hasNext() else None
#         return tmp
#
#     def hasNext(self):
#         return self.buffer is not None


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].