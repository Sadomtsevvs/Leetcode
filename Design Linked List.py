class MyLinkedList:

    def __init__(self, x=None, n=None):
        self.val = x
        self.next = n

    def get(self, index: int) -> int:
        # check if there is no nodes in object
        if self.val is None:
            return -1
        # create a parent node
        cur = MyLinkedList(None, self)
        for i in range(index + 1):
            cur = cur.next
            if not cur:
                return -1
        return cur.val

    def addAtHead(self, val: int) -> None:
        if self.val is not None:
            prev_head = MyLinkedList(self.val, self.next)
            self.next = prev_head
        self.val = val

    def addAtTail(self, val: int) -> None:
        if self.val is not None:
            cur = self
            while cur.next:
                cur = cur.next
            cur.next = MyLinkedList(val, None)
        else:
            self.val = val

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        cur_index = 0
        prev = None
        cur = self
        while cur.next and cur_index < index:
            prev = cur
            cur = cur.next
            cur_index += 1
        if cur_index + 1 == index:
            cur.next = MyLinkedList(val, None)
        elif cur_index == index:
            prev.next = MyLinkedList(val, cur)

    def deleteAtIndex(self, index: int) -> None:
        if self.val is None:
            return
        if index == 0:
            if self.next:
                self.val, self.next = self.next.val, self.next.next
            else:
                self.val, self.next = None, None
            return
        cur_index = 0
        prev = None
        cur = self
        while cur.next and cur_index < index:
            prev = cur
            cur = cur.next
            cur_index += 1
        if cur_index == index:
            prev.next = cur.next


# There are better solutions in LC comments:
# they have attribute "length", so we don't need to seek every time
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class MyLinkedList:
# 
#     def __init__(self):
#         self.dummy = ListNode()
#         self.length = 0

obj = MyLinkedList()
obj.addAtHead(2)
obj.deleteAtIndex(1)
print(1)
