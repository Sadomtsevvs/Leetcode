"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        if head.next == head:
            node = Node(insertVal, head)
            head.next = node
            return head
        prev = None
        cur = head
        while cur.val <= cur.next.val:
            prev = cur
            cur = cur.next
            if cur == head:
                break  # cycle
        prev = cur
        cur = cur.next
        # cur is the smallest now, prev is the biggest
        if insertVal <= cur.val or insertVal >= prev.val:
            node = Node(insertVal, cur)
            prev.next = node
            return head
        while cur.val <= insertVal:
            prev = cur
            cur = cur.next
        node = Node(insertVal, cur)
        prev.next = node
        return head

        # official solution
        #
        # if head == None:
        #     newNode = Node(insertVal, None)
        #     newNode.next = newNode
        #     return newNode
        #
        # prev, curr = head, head.next
        # toInsert = False
        #
        # while True:
        #
        #     if prev.val <= insertVal <= curr.val:
        #         # Case #1.
        #         toInsert = True
        #     elif prev.val > curr.val:
        #         # Case #2. where we locate the tail element
        #         # 'prev' points to the tail, i.e. the largest element!
        #         if insertVal >= prev.val or insertVal <= curr.val:
        #             toInsert = True
        #
        #     if toInsert:
        #         prev.next = Node(insertVal, curr)
        #         # mission accomplished
        #         return head
        #
        #     prev, curr = curr, curr.next
        #     # loop condition
        #     if prev == head:
        #         break
        # # Case #3.
        # # did not insert the node in the loop
        # prev.next = Node(insertVal, curr)
        # return head

        # concise solution from LC
        #
        # node = Node(insertVal)
        #
        # if not head:
        #     node.next = node
        #     return node
        #
        # prev, curr = head, head.next
        #
        # while prev.next != head:
        #     # Case1: 1 <- Node(2) <- 3
        #     if prev.val <= node.val <= curr.val:
        #         break
        #
        #     # Case2: 3 -> 1, 3 -> Node(4) -> 1, 3 -> Node(0) -> 1
        #     if prev.val > curr.val and (node.val > prev.val or node.val < curr.val):
        #         break
        #
        #     prev, curr = prev.next, curr.next
        #
        # # Insert node.
        # node.next = curr
        # prev.next = node
        #
        # return head