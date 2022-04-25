class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyQueue:

    def __init__(self):
        self.first = None
        self.last = None

    def push(self, x: int) -> None:
        new = ListNode(x)
        if not self.last:
            self.first = new
            self.last = new
        else:
            self.last.next = new
            self.last = new

    def pop(self) -> int:
        get, self.first = self.first, self.first.next
        if not self.first:
            self.last = self.first
        return get.val

    def peek(self) -> int:
        return self.first.val

    def empty(self) -> bool:
        return not self.first

# official solution
#
# class MyQueue:
#     def __init__(self):
#         self.s1 = []
#         self.s2 = []
#
#     def push(self, x):
#         self.s1.append(x)
#
#     def pop(self):
#         self.peek()
#         return self.s2.pop()
#
#     def peek(self):
#         if not self.s2:
#             while self.s1:
#                 self.s2.append(self.s1.pop())
#         return self.s2[-1]
#
#     def empty(self):
#         return not self.s1 and not self.s2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
